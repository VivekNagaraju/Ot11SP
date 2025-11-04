'''
Created on 04-Nov-2025

@author: Vivek

Argument: A variable defined in function definition and values passed when a function is called
            are called as arguments

1. Formal arguments: A variable defined in function definition
2. Actual arguments: values passed when a function is called

Ex:
def add(a, b): 
    c=a+b
    return c
    
add(1, 4)

a, b --> Formal arguments
1, 4 --> Actual arguments

Types of arguments:

- Actual arguments
    1. Positional arguments
    2. Keyword arguments
    
- Formal arguments:
    1. default arguments
'''
def add(a=0, b=0): 
    c=a+b
    print(f"Sum of {a} and {b} is", c)

add(4, 5) # Positional arguments
add(6, 4)
add(b=10, a=20) # keyword arguments
add()
add(4)
