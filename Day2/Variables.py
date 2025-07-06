# Variables
a = 15
s = "rony"

#A will not overwrite a, variables are case sensitive
A = "Rony"
print("My name is", A)
# type conversion
f = float(a)

print("a, s, f = ", a, s, f)

#checking the type of variable
print("Type of variable a", type(a))

# User input--> by default input is of type string
var = input("Enter Something it will be store on var: = ")
print("Type of var is = ", type(var))
print("By default user input is a string, here var is a string: ", var)

# Taking input of different data type
a = int(input("Enter number a: = "))
b = int(input("Enter number b: = "))

# We can add similar datatype, otherwise it will show error
print("a + b = ", (a+b))

# Assign multiple variables together
x, y, z = "apple", "banana", "orange"
print("Some of the delicious fruits are: ", x ,",",y,",",z)


# Unpacking
fruits = ["apple", "banana", "cherry"] #list
# Unpack list
x, y, z = fruits
print("Unpacking fruits:")
print(x)
print(y)
print(z)


# One value to multiple variables
print("One value to multiple variables:")
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Global variables-> Variables declared outside of any functions are global
# Variables used till now is global, it can be used any where

def myfunc():
   print("Acessing global variable x, y, z inside a function. x, y, z is = ", x, y, z)
   # local variable
   var2 = 35
   # this can be accessed outside of the function
   # global var3 = 55, we can't do this
   global var3
   var3 = 55
   print("Var2 inside of the function: ", var2)

# Calling function
myfunc()

# We can't acess variable of a function outside of that function
# print("Var2 outside of the function: ", var2)

print("Var3 outside of the function: ", var3)

