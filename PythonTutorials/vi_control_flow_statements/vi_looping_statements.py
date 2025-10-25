'''
Created on 23-Oct-2025

@author: Vivek

"Reduce repetation - increase reuse" --> Easy maintenence

Looping statements: 
- Looping statements are used to execute any statement/s repeatedly.
- Any statement/s will be executed repeatedly until a condition is fulfilled

Types of Looping Statements:
1. While loop:
    - initial variable -- used to set initial value
    - define the condition
    - increment/ decrement
    
2. For loop: Is used to iterate over a sequence/ range

range(1, 10, 3) - 1, 4, 7


Loop control statements:
1. break - stop loop execution in between
2. continue - skips the execution of statements in a loop available after continue statement once


105 - chethan


'''

'''
count = 0 # initial variable

while count < 5: # condition
    print("Hello world!")
    # count = count + 1 # increment
    count+=1 # increment
'''
'''
count = 5 # initial variable

while count > 0: # condition
    print("Hello world!")
    # count = count - 1 # decrement
    count-=1 # decrement
    
'''
# Infinite Loops
'''
while True:
    print("Hello world!")
'''    
'''    
while 1==1:
    print("Hello world!")
    
'''

# print(range(4))
'''
for i in range(1, 100):
    print(i)
    if i == 50:
        break
    
'''

'''
num=1
while True:
    
    print(num)
    num+=1
    if num==51:
        break
        
'''
'''
for i in range(1, 100):
    if i == 50:
        continue
    print(i)
'''   

num=1
while num<100:
    if num == 50:
        num+=1
        continue
    print(num)
    num+=1