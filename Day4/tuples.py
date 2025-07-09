# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Similar to list

# Create a tuple

tuple1 = ("a", 3, 5, 6, 7, 78)
print("Tuple 1 = ",tuple1)

# As tupule is unchangeble we can't change the value of an index
# tuple1[0] = 0 (this will through error)
print("tuple1[0] =",tuple1[0])

# Updating tuples with the help of list
x = ("apple", "banana", "cherry")
print("tuple x = ",x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("Updating tuples with the help of list",x)

# We can't append like list, if we need then convert tuple to list then append and convertback

# Append using two tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",) #for single tuple we must use comma
print("This tuple before append = ",thistuple)
thistuple += y
print("Thistuple after append",thistuple)


# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print("Unpacking list into variables")
print(green)
print(yellow)
print(red)


# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Lopp through tuple
tuple5 = ("apple", "banana", "cherry")
print("Printing items using loop")
for i in range(len(tuple5)):
  print(tuple5[i])