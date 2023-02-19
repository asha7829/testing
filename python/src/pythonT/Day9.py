'''
Created on 26-Jan-2023

@author: Asha
'''
#modules and packages

"""module is collection of function,class(variable+methods) developer will write all the function and feature in one module work will be divided
finally it will intergrate in one module"""
#writing the function and class in one module and we can call them in other module2
#day9 is module 

def add(num1,num2):
    print(num1+num2)
def mul(num1,num2):
    print(num1*num2)
    
#same function day9,module2,module3
def animal():
    print("animal cant fly")
def bird():
    print("bird color is white")   
    
    
#using class and function  

class Animal:
    def display(self):
        print("animal can walk")   
        
        
"""import using module name (approch 1)
from module import function,classes (calling the object)(approch 2)"""

#package can have multiple packages
#:-collection of modules

#package--->module-->function and classes

"""module1-->function.
module2-->function.
both are one package in one CreateFolder
new folder i need to call the package we use sys funtion
#approch 1
import sys
sys.path.append(package url)
import module1
import module2

module1.display()
module2.show()"""
"""
#approch 2
from module1 import *
from module2 import *"""

display()
show()


