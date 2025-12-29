'''
Created on 29-Dec-2025

@author: Vivek

Regular Expressions: Defines the pattern of a string

"ab" --> exact match
"[ab]" --> a or b
"[^ab]" --> except a and b
[a-z] --> any lower case letter
[A-Z] --> any upper case letter
[a-zA-Z] --> any alphabet
[0-9] --> any integer from 0 to 9
[a-zA-Z0-9] --> aplhanumeric character
[^a-zA-Z0-9] --> special character
'''
import re

pattern = re.compile("[^ab]")
matcher = pattern.finditer("hgcabjagabajauehab")
# matcher = re.finditer("ab", "hgcabjagabajauehab")
print(matcher)

count=0
for i in matcher:
    # print(i)
    print("Start index:", i.start())
    # print("Stop index:", i.end())
    print("Character:", i.group())
    count+=1
    
print(count)

'''
'''
    