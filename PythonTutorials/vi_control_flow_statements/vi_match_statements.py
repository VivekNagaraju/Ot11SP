'''
Created on 25-Oct-2025

@author: Vivek
'''
number = int(input("Please enter day number:"))

match number:
    case 1:
        print("1 represents Monday")
        
    case 2:
        print("2 represents Tuesday")
        
    case 3:
        print("3 represents Wednesday")
        
    case 4:
        print("4 represents Thursday")
        
    case 5:
        print("5 represents Friday")
        
    case 6:
        print("6 represents Saturday")
        
    case 7:
        print("7 represents Sunday")
        
    case _ :
        print("Please enter integer from 1 to 7")