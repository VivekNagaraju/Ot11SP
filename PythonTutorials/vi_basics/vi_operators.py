'''
Created on 14-Oct-2025

@author: Vivek

Operator: Is a symbol which performs operation on one or more operands(variables)

I. Classification of operators based on No. of operands:
    1. Unary operator: acts on single operand
        Ex: =, -
    2. Binary Operator: acts on two operands
        Ex: +, - etc.,
    3. Ternary Operator: acts on three operands
        Ex: list comprehension

II. Classification of operators based on Operations:
    1. Arithmetic Operators: +, -, *, /(Quotient), %(Reminder), ** (Exponent), // (Floor division)
        i/p: numerical
        o/p: numerical
        
    2. Comparison/ Relational Operators: >, <, >=, <=, !=, ==
        i/p: numerical
        o/p: boolean
        
    3. Assignment Operator: =
    4. Logical Operators: AND, OR, NOT
        i/p: boolean (True/ False)
        o/p: boolean
        
        AND(both): If 'a' AND 'b' is True, o/p will be True. Takes 2 i/ps
        OR(anyone): If any of the i/p is True, o/p will be True. Takes 2 i/ps
        NOT (reverse): If i/p is True o/p will be False and vice-versa. Takes 1 i/p
        
    5. Membership Operators: To check  whether any element is part of a group
        -- in, not in
    6. Identity Operators: To check identity/ to check whether 2 variables are identical
        -- is , is not
    7. Unary Minus operator: To negate the numbers
    
    String formatting/ formulazing
'''
print("=======Arithmetic Operators=========")
a = 27
b = 3
print(f"Sum of {a} and {b}:", a+b)
print("a-b:", a-b)
print("a*b:", a*b)
print("a/b:", a/b)
print("20.0/3:", 20.0/3)
print("a%b:", a%b)
print("a**b:", a**b)
print("a//b:", a//b)
print("20.0//3:", 20.0//3)

print("========Comparison/ Relational Operators=======")
print("a>b:", a>b)
print("a<b:", a<b)
print("a>=b:", a>=b)
print("a<=b:", a<=b)
print("a==b:", a==b)
print("a!=b:", a!=b)

print("=========Logical Operators===========")
print("=====AND Operator=====")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

print("=====OR Operator=====")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

print("======NOT Operator======")
print("not True: ", not True)
print("not False: ", not False)

print("======Membership Operators======")
print("'i' in 'vivek':",'i' in 'vivek')
print("'I' in 'vivek':",'I' in 'vivek')
print("'z' in 'vivek':",'z' in 'vivek')
print("'z' not in 'vivek':",'z' not in 'vivek')

print("======Identity Operators======")
name1 = 'vivek'
name2 = 'vivek'
print(id(name1))
print(id(name2))

print("name1 is name2: ", name1 is name2)
print("name1 is not name2: ", name1 is not name2)

# print("'Vivek' is 'vivek': ",'Vivek' is 'vivek')
# print("'Vivek' is not 'vivek': ",'Vivek' is not 'vivek')
