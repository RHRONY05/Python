# Assign string, using '' or "" or ''' '''
a = "Hello, world"
print("Single line string: = ", a)

# Iterate through string
print("Printing string a using loop:")
for x in a:
   print(x)

# Multiline string
b = """Twinkle Twinkle little star 
 How i wonder what you are!"""
print("Multiline string:= \n",b)

# length of string
print("length of string b: ",len(b))

# string indexing(we can acess string using both positive and negative index, positive index starts from "0", negative starts from '-len()')
print("Acessing string using positive index-> a[0], a[1],a[2] = ", a[0],",", a[1],",", a[2],",")
print("Acessing string using negative index-> a[-1], a[-2],a[-3] = ", a[-1],",", a[-2],",", a[-3],",")

# Slicing string
print("Slicing string a from 1 to 5",a[1:5])
print("Slicing string a from 0 to 5",a[:5])
print("Slicing string a from 0 to end",a[0:])

# Converting to upper case and lowercase
s = "Atik"
print("Upercase",s.upper())
print("Lowercase",s.lower())

# Spliting string into two
print("Splitting Hello, World! after comma", a.split(","))

# Replace
print("Replace t of Atik with sh->", s.replace('t','sh'))

# Remove white spaces from start and end
white_space = "   Bangladesh is a small country "
print("Before removing whitespace from start and end, white_space ->",white_space)
print("After removing whitespace from start and end, white_space becomes->",white_space.strip())

# check if substring is present substring
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

if "Tahsin" not in txt:
   print("No, Tahsin is not present in txt")

   