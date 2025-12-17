'''
Created on 16-Dec-2025

@author: Vivek

Inheritance: Is passing of properties(variables/ functions) from one class to another class.
Parent/ Super class: Class from which properties are inherited Ex: GrandFather
Child/ sub class: Class which inherits the properties Ex: Father

Using the object of Child class Parent class properties can be accessed

Types of Inheritance:
1. Single-level inheritance
2. Multi-level inheritance
3. Multiple inheritance

Method Resolution Order: mro()
'''
class GrandFather:
    def __init__(self):
        print("This is GF's constructor")
        
    def gf_method(self):
        print("This is GrandFather class method")
        
    def home(self):
        print("This is GF's home")
        
class Father(GrandFather):
    def f_method(self):
        print("This is Father class method")
    
    def home(self):
        print("This is Father's home")
        
class Mother:
    def m_method(self):
        print("This is Mother class method")
        
    def home(self):
        print("This is Mother's home")
        
class Child(Father, Mother):
    def c_method(self):
        print("This is Child class method")
    
    def home(self):
        print("This is Child's home")
        
ajja = GrandFather()
ajja.gf_method()

appa = Father()
appa.f_method()
appa.gf_method()

nanu = Child()
nanu.c_method()
nanu.f_method()
nanu.gf_method()
nanu.m_method()
nanu.home()

'''
print(Child.mro())
print(dir(nanu))
'''