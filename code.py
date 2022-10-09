print("Hello world")
# This is a single line comment

'''This is multi-line comment.
We can add as many lines we want.
Comment will be stay inside of triple string or triple quote.
Comment is most important for clean code, 
which is required for documentation and future reference.'''

# Creating variables
x=5
y="Jhon"
print(x)
print(y)
x=4
x="Sally"
print(x)
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# Variable Names
myvar = "Jhon"
my_var = "John"
_my_var = "Jhon"
myVar = "Jhon"
MYVAR = "Jhon"
myvar2 = "Jhon"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi words variable names:
#(1. Camel Case)
myVariableName = "Camel Case"
print(myVariableName)
#(2. Pascal Case)
MyVariableName = "Pascal case"
print(MyVariableName)
#(3. Snake Case)
my_variable_name = "Snake Case"
print(my_variable_name)

# Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)
# In the print()function,
# you output multiple variables, separated by comma:
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)
x = "I'm"
y = "Full-Stack"
z = "Developer"
print(x,y,z)
# You can also use the + operator to output the multiple variables:
x = "InShallah I will get, "
y = "Python developer soon. "
z = "As a graduate."
print(x+y+z)

# For numbers, the + character work as a mathematical operator:
x = 5
y = 10
z = 20
print(x+y+z)
# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
'''
x = 5
y = "Jhon"
print(x + y)
'''
'''The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:'''
x = 5
y = "Jhon"
print(x, y)

