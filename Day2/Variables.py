# Variables
a = 15
s = "rony"
# type conversion
f = float(a)

print("a, s, f = ", a, s, f)

#checking the type of variable
print("Type of variable a", type(a))

# User input--> by default input is of type string
var = input("User input: = ")
print("Type of var is = ", type(var))
print("By default user input is a string, here var is a string: ", var)

# Taking input of different data type
a = int(input("Enter number a: = "))
b = int(input("Enter number b: = "))

# We can add similar datatype, otherwise it will show error
print("a + b = ", (a+b))
