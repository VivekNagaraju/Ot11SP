'''
Created on 10-Nov-2025

@author: Vivek

Types of variables:
 
In python variables are divided into categories as below based on their scope:

1. Local/ method variables: 
    - Variables scope is restricted to one particular method
    - Variable value can change one method to another method
    - Access:
        within a method with same name
    
2. Instance/ object variables: 
    - scope: object level, 
    - but can be used in multiple methods
    - change from one object to another object
    Access:
    - within a class--> self.variable_name
    - outside of a class --> obj_name.variable_name
    
3. Static/ class variables:
    - Scope: class level, values remains same for all the objects of that class
    - it will not change 
    Access:
    - within a class/ outside of a class --> ClassName.variable_name
    
4. Global variable:
    - declared outside of a class
    - can be accessed anywhere in that module

'''
# day="Monday" # Global variable

class Student:
    school_name = "iQuest" # Static/ class variable
    global day 
    day = "Monday" # Global variable
    
    def __init__(self, name, roll_no):
        self.name = name # Instance/ object variable
        self.roll_no = roll_no
        # Student.school_name = "iQuest" # # Static/ class variable
        
    def display_details(self):
        print("Student name:", self.name)
        print("Roll No.:", self.roll_no)
        print("School Name:", Student.school_name)
        print("Day", day)
        # Student.school_name = "iQuest" # # Static/ class variable
        
    def calculate_marks(self, kan, eng, maths):
        total_marks = kan+eng+maths # Local variable/ method variable
        self.total_marks = total_marks
        print("Total marks:", total_marks)
        # return total_marks
        
    def display_result(self):
        if self.total_marks>35:
            print("PASS :)")
        else:
            print("FAIL :(")