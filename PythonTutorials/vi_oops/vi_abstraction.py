'''
Created on 21-Dec-2025

@author: Vivek

Abstraction: 

Implemented methods/ concrete methods- It has both method name and method body
Un-implemented methods- It has method name but not method body

Abstract Class: class containing atleast one abstract method

Interface: class which contains abstract methods only
'''
from abc import abstractmethod, ABC

class HumanBeings(ABC):
    def eating(self): # Implemented method
        print("I'm eating")
    
    @abstractmethod  
    def facial_hair(self): # Un-implemented method
        pass
    
class Female(HumanBeings):
    
    def facial_hair(self):
        print("Thin facial hair")
    
    def dummy_method(self):
        print("Example")

# obj1 = HumanBeings() # TypeError: Can't instantiate abstract class HumanBeings with abstract method facial_hair

obj2 = Female()
obj2.eating()
# obj2.facial_hair()