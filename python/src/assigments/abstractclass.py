'''
Created on 22-Jan-2023

@author: Asha
'''
"""Create an abstract class ‘Parent’ with a method ‘message’. 
It has two subclasses each having a method with the same name ‘message’ that prints. 
“This is first subclass” and “This is second subclass” respectively. Call the methods ‘message’ by creating an object for each subclass."""
"""from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def message(self):
        pass
class father(parent):
    def message(self):
        print("jklsjdjs")
class mother(parent):
    def message(self):
        print("gjhskdsdhhus")
a=father()
a.message()
a1=mother()
a1.message() """
"""Python Tutorial 25 - Abstraction in Python"""
"""Abstract Class and Abstract Method in Python(Telusko)"""
"""two abstract method 
from abc import ABC,abstractmethod  
class animal(ABC):
    @abstractmethod
    def message(self):
        pass
    @abstractmethod
    def m1(self):
        pass
class father(animal):
    def message(self):
        print("jklsjdjs") #TypeError: Can't instantiate abstract class father with abstract method m1
    def m1(self):
        print("fgksdsd") 
           
a=father()
a.message()

we can use constructer in abstract class"""
"""from abc import ABC,abstractmethod 
class cal(ABC):
    def __init__(self,value):
        self.value=value
        
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class c(cal): 
    def add(self):
        print(self.value+10)
    def sub(self):
        print(self.value-20)
a=c(60)
a.add()
a.sub()   """

"""abstract class has one or more methods.
abstract method that is declear"""  
"""Summary:
abstract method is a method which only has declaration and doesn't have definition.
a class is called abstract class only if it has at least one abstract method.
when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
if it is not done then child class also becomes abstract class automatically.
at last, python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract."""               
                   