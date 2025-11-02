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
    a. Using Index:  List supports indexing
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
            
    b. Using loops
    c. Using slicing operator - to access multiple/ group of elements from a DS
    Syntax: list_name[start : stop : step]
    -> start - start index (included), default = 0*
    -> stop - stop index (excluded), default = len(list)
    -> step - increment/ decrement, default = 1
    
2. Modification: List is mutable (modifiable)
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
    
    
'''While loop'''

print("=========Accessing using while loop===========")
'''
print(list4[0])
print(list4[1])
print(list4[2])....
'''
i=0

while i<len(list4):
    print(list4[i])
    i+=1

print("=======Slicing Operator========")
print("list4=",list4)
print("list4[0:4]=", list4[0:4])
print("list4[::]=", list4[::])
print("list4[:7:]=", list4[:7:])


print("======Functions specific to Lists==========")
print("list4=",list4)
list4.append(78)
print("list4=",list4)
list4.append(list2)
print("list4=",list4)
print("list3=", list3)
list3.clear()
print("list3=", list3)
list5 = list4.copy() # Copying/ cloning
print("list5=",list5)
print("id(list4):", id(list4))
print("id(list5):", id(list5))
print(list5.append(67))
print("list4=",list4)
print("list5=",list5)
list5[4]=False
print("list4=",list4)
print("list5=",list5)
print("list5.count(1):", list5.count(1))
print("list5.count(2):", list5.count(2))
list5.extend(list2)
print("list5=",list5)
print("list5.count(2):", list5.count(2))
print("list5[8]:",list5[8])
print("list5[9]:",list5[9])
print("list5[10]:",list5[10])
print("list5[8][1]:",list5[8][1])
print("list5.index(2):",list5.index(2))
print("list5.index(2, 2):",list5.index(2, 2))
# print("list5.index(2, 11):",list5.index(2, 11)) # ValueError: 2 is not in list

list5.insert(3, 100)
print("list5=", list5)

list5.remove(False)
print("list5=", list5)

print("list5.pop(5):",list5.pop(5))
print("list5=", list5)

print("list5.pop():",list5.pop()) # it removes the element from last index of the list
print("list5=", list5)

print("list5.remove(78):", list5.remove(78))
print("list5=", list5)

# print("list5.remove():", list5.remove()) # TypeError: list.remove() takes exactly one argument (0 given)
# print("list5=", list5)

list5.reverse()
print("list5=", list5)

list6 = [2, 3, 4, 5, 78, 65, 54, 63, 5, 8, 9]
print("list6:", list6)
list6.sort()
print("list6:", list6)

list6.sort(reverse=True)
print("list6:", list6)
list7=[]
for i in list6:
    if i%2 == 0:
        list7.append(i)
        
print("list7:",list7)

# List Comprehension:

list8 =[j for j in list6 if j%2==0]
print("list8:",list8)


'''
1. Present a list to the user which contains duplicate and unique elements
2. Take any element from the list as input from the user
3. Print how many number of times that element appears in the list
4. Print the indices of that element in the list

'''

list9 = list8 # Aliasing
print("list9:",list9)
print("id(list8):", id(list8))
print("id(list9):", id(list9))
list9[3]=100
print("list8:",list8)
print("list9:",list9)

print("list8 + list5:",list8 + list5) # extending list8 with list5
print("list8*2:", list8*2) # extending the same list twice
