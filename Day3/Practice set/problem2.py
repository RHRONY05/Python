# Detect double space in a string
s = "There  is a double space in this string, is it true?"

if "  " in s:
   print("There  is a double space in this string, it is true")


# Use find() to check for 'pq',
text = "rstpqxy"
index = text.find('pq')

if index != -1:
    print(f"Found 'pq' at index {index}")
else:
    print("Did not find 'pq' in the string.")
