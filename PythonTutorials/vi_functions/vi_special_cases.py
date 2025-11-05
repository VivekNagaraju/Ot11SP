'''
Created on 05-Nov-2025

@author: Vivek

4! = 4*3*2*1
   = 4*3!
   = 4*3*2!
   = 4*3*2*1!
   = 4*3*2*1*0!
   = 4*3*2*1*1
0! = 1

4*3!
3*2!
2*1!
'''
def factorial(a):
    if a == 0:
        result = 1
    else:
        result = a*factorial(a-1)
    return result
    
print(factorial(4))