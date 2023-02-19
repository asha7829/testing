'''
Created on 22-Jan-2023

@author: Asha
'''
"""Create a class ‘Degree’ having a method ‘getDegree’ that prints “I got a degree”.
 It has two subclasses namely ‘Undergraduate’ and ‘Postgraduate’ each having a method with the same name that prints “I am a Undergraduate” and “I am a Postgraduate” respectively. 
 Call the method by creating an object of each of the three classes."""
class Degree:
    def getdegree(self):
        print("i got degree")
class undergraduate:
    def getdegree(self):
        print("I am a Undergraduate")  
class Postgraduate:
    def getdegree(Self):
        print("I am a postgraduate") 
a=Postgraduate()
a.getdegree()
a1=undergraduate()
a1.getdegree()
a2=Degree()
a2.getdegree()
  
