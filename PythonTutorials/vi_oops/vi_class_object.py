'''
Created on 09-Nov-2025

@author: Vivek

Constructor: Special/magic method used to construct an object with specific features/properties
- Constructor is called implicitly when an Object is created
- Constructor can be called explicitly if required
- Constructor can be with parameters or without parameters
- Constructor can be defined by a user, if not python will have its own constructor created
'''

class DogClass:
    
    def __init__(self, name, color, gender, breed): # Constructor
        print(f"A dog- {name} is created with color:{color}, gender:{gender} and breed:{breed}")
        self.name = name
        self.color = color
        self.gender = gender
        self.breed = breed
     
    def bark(self): # Method
        # print(f"{self.name} is barking")
        print(f"Dog is barking")
        
# puppy = DogClass()
puppy = DogClass("Puppy","Brown", "Female", "German Sheperd")
# puppy.__init__("Puppies","Red", "Female", "German Sheperd")
puppy.bark()
print(type(puppy))

# ramana = DogClass()
ramana = DogClass("Ramana","Brown", "Male", "German Sheperd")
ramana.bark()
puppy.bark()
print("puppy.name:",puppy.name)
print("ramana.name:",ramana.name)
puppy.name = "Puppi"
print("puppy.name:",puppy.name)

print(dir(puppy))