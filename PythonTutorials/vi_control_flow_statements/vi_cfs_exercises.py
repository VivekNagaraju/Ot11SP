'''
Created on 26-Oct-2025

@author: Vivek

* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

'''

for j in range(6):
    for i in range(6):
        # print("*", end=" ")
        print("* * * * * *") # This only works when there is fixed number of "*"(values) in every row
    print() 

num=1
for j in range(6):
    for i in range(1, j+1):
        print(num, end=" ")
        num+=1
        
    print() 