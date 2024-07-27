# Module 12, Lab 12
# Mollee Kahan
# 7/27/24
#This program will store any amount of grades into a text file called "grades.txt"

class Pet:
    """Pet class for maintaing a pet's type and name"""

    def __init__(self):
        """initialize a pet object without arguments"""

        #sets preset values for name, type, age
        #3 attributes: name(str), type(str), age(int)
        self.name = ""
        self.type = ""
        self.age = 0

    #getter function for name
    def getName(self):
        """Return the name"""
        return self._name
    
    #gettter function for type
    def getType(self):
        """Return the type"""
        return self._type
    
    #getter function for age
    def getAge(self):
        """Return the age"""
        return self._age
    
    #setter function for name
    def setName(self,name):
        """Set the name"""
        #checks to make sure input is a string
        if name.isalpha() == False:
            raise ValueError('Name must be a string')
        #assigns new name to name
        self._name = name
    
    #setter function for type
    def setType(self,type):
        """Set the type"""
        #checks to make sure input is a string
        if type.isalpha() == False:
            raise ValueError('Type must be a string')
        #assigns new type to type
        self._type = type

    #setter function for age
    def setAge(self,age):
        """Set the age"""
        #checks to make sure input is an int that's larger than 0
        if age.isalpha() == True:
            raise ValueError('Age must be an int')
        if age <= 0:
            raise ValueError('Age must be larger than 0')
        #assigns new age to age
        self._age = int(age)

def main():
    """main function to create a pet object. Makes calls to Pet() class. """
    #instantiates a new Pet object called animal
    animal = Pet()
    
    #creates variables to store user's input
    userInputName = input("Enter your pet's name: ")
    userInputType = input("Enter your pet's type: ")
    userInputAge = input("Enter your pet's age: ")

    #calls to setter functions using user's input
    animal.setName(userInputName)
    animal.setType(userInputType)
    animal.setAge(userInputAge)
    
    #prints all 3 attributes of the pet object: animal
    print("The pet name is",animal.getName())
    print("The pet type is",animal.getType())
    print("The pet age is",animal.getAge())

#call to main function to run program
main()