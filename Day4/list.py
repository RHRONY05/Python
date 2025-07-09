# Unlike c++, list here can store data of multiple data types

# List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
list1 = ["abc", 34, True, 40, "male"]

print("List1 = ",list1)
# Acess list
print("List[2] = ",list1[2])

# list length
print("length of list1 =",len(list1))

# Sort list(sort is possible if data's are of same data type)
list2 = [7,8,2,4,9,1]
list2.sort()
print("Sorted list2 :",list2)

# Reverse list(We need to reverse first then we can print it)
list2.reverse()
print("Sorted list2 :",list2)

# Adding an element at the end
list2.append(10)
print("Appended 10 at the end of list2 :",list2)

# Insert an element anywhere in the list, insert(index,item)
list1.insert(2,"apple")
print("Insert apple at 2nd index of list1 :",list1)

# Print list as string
print("Print List as string : ", list1[1:3])

# Delete element from an specific position, pop(index you want to delete)
item = list1.pop(2) #it return the deleted item
print("item deleted from list1 =",item)
print("After deleting item from list1 =",list1)

# Search and delete element
list2.remove(9)
print("After deleting 9 from list2", list2)

# If we try to remove an element and that is not present it will through an error

# list2.remove(12)
# Handle error using try catch or if else

try:
   list2.remove(12)
   print("12 was removed from list2", list2)
except ValueError:
   print("12 is not present in list2",list2)   

if 2 in list2:
   list2.remove(2)
   print("2 was removed from list2", list2)
else: 
   print("2 is not present in list2",list2)


# Copy list
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
list3 = [17, 22, "abcd", True ,9]
list4 = list3
print("list3 and list4 = ",list3,list4)
# Any change on list4 will change 3 and vice-versa
list4.append(13)
print("list4 was changed so list3 should get changed",list3,list4)

# To copy list without reference
thislist = ["apple", "banana", "cherry"]
print("thislist",thislist)
mylist = thislist.copy()
print("Copying thislist into mylist",mylist)

# Change in copy list doesn't have any effect on original list
mylist.append("Orange")
print(f"""
Change in mylist doesn't have any effect on thislist : 
mylist after change = {mylist}
thislist after changing mylist = {thislist}
""")

# Joining two list
# Easy way, we can also join through loop using list.append(x)
list = list1 + list2
print("list1 and list2 from the begining was joined together",list)