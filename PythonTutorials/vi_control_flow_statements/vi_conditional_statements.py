'''
Created on 16-Oct-2025

@author: Vivek

Indentation: It is the leading space to define a block of code
1 Indentation = 1 tab space = 4 normal spaces

Conditional statements: Flow of program execution will be decided based on a condition.
(Decision-making statements)

1. if statement
2. if-else statement
3. Series if-else statements
4. Nested if-else statements
'''
# age = int(input("Please enter your age:"))

'''
if age>12:
    print("Age is satisfied")
else:
    print("Age is not satisfied")

print("Program terminated")
'''
'''
if age>0:
    if age<=3:
        print("You're a toddler")
    elif age<=12:
        print("You're a child")
    elif age<=18:
        print("You're a teenager")
    elif age<=60:
        print("You're an adult")
    else:
        print("You're senior citizen")
else:
    print("Please enter positive number")
'''
year = int(input("Please enter a Year in YYYY format:"))

if year%100 == 0:
    if year%400 == 0:
        print(f"{year} is a leap year")
    
    else:
        print(f"{year} is not a leap year")

else:
    if year%4 == 0:
        print(f"{year} is a leap year")
    
    else:
        print(f"{year} is not a leap year")

