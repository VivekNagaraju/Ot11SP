'''
Created on 27-Oct-2025

@author: Vivek

List: 

- List is a DS where elements stored within square braces separated by commas
1. Creation:
    - Empty list can be created
    - List with elements:
        > Manual entry
        > Using built-in function - list()/ tuple()/ set()
'''

list1 = []
print("list1:", list1)
print(type(list1))

list2 = [2, 5, 6, 8, 4] # Manually entering elements in the list
print("list2:", list2)
print(type(list2))

list3 = list(range(6))
print("list3:", list3)
print(type(list3))