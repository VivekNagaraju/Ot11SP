'''
Created on 16-Dec-2025

@author: Vivek

Inheritance: Is passing of properties(variables/ functions) from one class to another class.
Parent/ Super class: Class from which properties are inherited Ex: GrandFather
Child/ sub class: Class which inherits the properties Ex: Father
'''
class GrandFather:
    def gf_method(self):
        print("This is GrandFather class method")
        
class Father(GrandFather):
    def f_method(self):
        print("This is Father class method")
        
ajja = GrandFather()
ajja.gf_method()

appa = Father()
appa.f_method()
appa.gf_method()