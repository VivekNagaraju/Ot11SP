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
    - List is heterogeneous: List stores all fundamental data-types including None type
    
2. Accessing the elements:
    - Using Index:  List supports indexing
        Index is a number which represents a position in a DS
        - Positive Index: 
            > Numbering the positions from left-to-right ( --> )
            > Index starts with 0, 1, 2....
            
        - Negative Index:
            > Numbering the positions from right-to-left ( <-- )
            > Index starts with -1, -2, -3....
            
        - Syntax: ds_name[index] --> this will return the value present in that index
        
        - We get IndexError in following cases
            > Using index greater than or equal to length of the list. Ex: list4[7]
            > Using index lesser than the negative value of length of the list. Ex: list4[-8]
            
    - Using loops
    - Using slicing operator
'''

list1 = []
print("list1:", list1)
print(type(list1))



list2 = [2, 5, 6, 8, 4] # Manually entering elements in the list # homogeneous list
print("list2:", list2)
print(type(list2))

list3 = list(range(6))
print("list3:", list3)
print(type(list3))

list4 = [1, 2, 3.0, 5+6j, True, "Vivek", None] # heterogeneous list
print("list4:", list4)
print(type(list4))

'''Accessing using Index'''
print("list4[3]:",list4[3])
print("list4[-3]:",list4[-3])

# print("list4[7]:",list4[7]) # IndexError: list index out of range
# print("list4[-8]:",list4[-8]) # IndexError: list index out of range

print("Length of list4:", len(list4))


'''Accessing using Loops'''

'''For loop'''

for i in list4:
    print(i)
