# pip install requests beautifulsoup4 lxml pandas gspread google-auth

import re, csv, sys, time
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd

URL = "https://www.geeksforgeeks.org/dsa/dsa-sheet-by-love-babbar/"

TOPIC_NAMES = [
    "Arrays","Matrix","Strings","Searching and Sorting","LinkedList",
    "Bit Manipulation","Greedy","Backtracking","Dynamic Programming",
    "Stacks and Queues","Binary Trees","Binary Search Tree","Graphs",
    "Heap","Trie"
]

def get_soup(url):
    # polite headers + retries
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/118.0 Safari/537.36"
    }
    for i in range(5):
        r = requests.get(url, headers=headers, timeout=30)
        if r.ok and len(r.text) > 5_000:
            return BeautifulSoup(r.text, "lxml")
        time.sleep(1 + i)
    r.raise_for_status()

def clean_text(t):
    t = re.sub(r"\s+", " ", t or "").strip()
    # Normalize some variants seen on the page
    t = t.replace("no.", "no.").replace("  ", " ")
    return t

def is_topic_heading(tag):
    if not isinstance(tag, Tag): return False
    if tag.name in ("h2","h3","h4"):
        txt = clean_text(tag.get_text())
        for nm in TOPIC_NAMES:
            if txt.lower().startswith(nm.lower()):
                return True
    return False

def extract_table_questions(tbl):
    titles = []
    for tr in tbl.find_all("tr"):
        tds = tr.find_all("td")
        if not tds: 
            continue
        # usually 1st column is the question title
        title = clean_text(tds[0].get_text(" ", strip=True))
        if title and title.lower() != "question":
            titles.append(title)
    return titles

def extract_inline_block_questions(container):
    """
    Fallback: sometimes the page shows lines like
    'Reverse an Array/String Link Link' as inline elements.
    We capture the leading text before first link on each line.
    """
    titles = []
    for br in container.find_all(["p","li","div"]):
        line = clean_text(br.get_text(" ", strip=True))
        # Heuristics: must contain at least 2-3 words and not be a heading
        if line and len(line.split()) >= 3 and not any(h in line for h in ("Question Article Practice",)):
            # Attempt to cut trailing 'Link Link' markers if present
            line = re.sub(r"\s*Link(\s*Link)?\s*$", "", line, flags=re.I)
            # Avoid pure “Link” rows
            if not re.fullmatch(r"Link", line, flags=re.I):
                # avoid lines that are just "NA" etc.
                if not re.fullmatch(r"(NA|na)", line):
                    titles.append(line)
    return titles

def scrape():
    soup = get_soup(URL)

    # Map: Topic -> list of titles
    result = {t: [] for t in TOPIC_NAMES}

    # Find all headings that are topics
    headings = [h for h in soup.find_all(is_topic_heading)]
    # To define section bounds, pair each heading with the next heading
    for idx, h in enumerate(headings):
        # Determine topic name normalized
        htxt = clean_text(h.get_text())
        topic = None
        for nm in TOPIC_NAMES:
            if htxt.lower().startswith(nm.lower()):
                topic = nm
                break
        if not topic:
            continue

        # Section slice = siblings until next topic heading
        section_nodes = []
        nxt = headings[idx+1] if idx+1 < len(headings) else None
        cur = h.next_sibling
        while cur and cur is not nxt:
            section_nodes.append(cur)
            cur = cur.next_sibling

        # First try: tables
        titles = []
        for node in section_nodes:
            if isinstance(node, Tag) and node.name == "table":
                titles.extend(extract_table_questions(node))

        # Fallback: inline blocks if no tables captured (some pages render without <table>)
        if not titles:
            wrapper = BeautifulSoup("<div></div>", "lxml").div
            for n in section_nodes:
                if isinstance(n, Tag):
                    wrapper.append(n)
            titles = extract_inline_block_questions(wrapper)

        # Light cleanup: drop obvious noise and duplicates
        clean_titles = []
        for t in titles:
            t = clean_text(t)
            if not t: 
                continue
            # remove "Question Article Practice" header lines, and lines that are just links
            if t.lower().startswith("question article"): 
                continue
            # trim trailing " [V. IMP]" etc. but keep core title
            t = re.sub(r"\s*\[[^\]]*\]\s*$", "", t).strip()
            if t and t not in clean_titles:
                clean_titles.append(t)

        result[topic].extend(clean_titles)

    # Build DataFrame
    rows = []
    for topic in TOPIC_NAMES:
        for title in result.get(topic, []):
            rows.append({
                "Topic": topic,
                "Problem Title": title,
                "Status": "TODO",
                "Learnings": ""
            })

    df = pd.DataFrame(rows)

    # Basic sanity: remove exact duplicates
    df.drop_duplicates(subset=["Topic","Problem Title"], inplace=True, ignore_index=True)

    # Save CSV
    csv_path = "love_babbar_450_gfg.csv"
    df.to_csv(csv_path, index=False, quoting=csv.QUOTE_MINIMAL)

    # Report
    print("Saved:", csv_path)
    by_topic = df.groupby("Topic")["Problem Title"].count().to_dict()
    print("Counts by topic:", by_topic)
    print("Total problems:", len(df))

    # If the page layout changes and you get fewer than ~400 rows, alert:
    if len(df) < 400:
        print("\nWARNING: Extracted fewer than 400 problems.",
              "The page layout may have changed. Inspect selectors or rerun.", file=sys.stderr)

if __name__ == "__main__":
    scrape()
