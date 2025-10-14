'''
Created on 12-Oct-2025

@author:N, Vivek 

Variables: Name given to the container in a memory location which stores data(input/ output)

Data stored in the location/ container can be changed.

syntax:

variable_name = value

Invalid cases:
1. While defining the variables Variable name should always be in Left Hand Side and value should
    be in right hand side
2. Variable name should start with a character/ letter. It should not start with numbers
3. Numerical values should not start with 0

Comments: Which gives description about single line/ block of a code

Types of comments:
1. Single line comments, #
2. Multi-line comments, triple-single quotes/ triple-double quotes
'''

# Defining one variable at a time --> Single line comment
num1 = 23
num2 = 34.5
num3 = 4+5j
name = 'Vivek'
print(num1)
# print(id(num1))

# Defining multiple variables in single line
num4, num5, num6 = 45, 67.8, 2+8j
print("num4:", num4)
# print(id(num4))
print(num5)
# print(id(num5))
print(num6)
# print(id(num6))

num7 = num8 = 10
print(num7, num8)
# print(id(num7))
# print(num8)
# print(id(num8))

'''
num8=20
print(num8)
print(id(num8))
'''




