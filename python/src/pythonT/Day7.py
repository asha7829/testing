'''
Created on 29-Jan-2023

@author: Asha
'''
""""c-->object oriented
c++-->object oriented
java--->object oriented
python--->is structured + object oriented ( with out class we can write prgm is structured),,,(object oreiented means with class..) """

#oops(object orietend programming concept)
#1)class
#2)object
#3)inhertance
#4)polymorphism

"""class means employees working in one company is called class animal group is class"""
"""class is employees and object is name asha, reetu,different salary and designa is object""" #dog is class object is dog,cat,elep
"""class -->collection of variables(attributes)&methods(behavior):
class is logical entity object is physical entity
A class is blueprint
logical Entity
does not copy space in the memory

object--->is an instance of class obj=
physical entity
which occupy the space in memory

for one class we can create multiple Objects
object are independent

function vs method
function-->we can create without class
method-->create inside the class"""


"""class myclass():
    def myfun(self):
        pass
    def display(self):
        print("john")
        
obj=myclass()
obj.myfun()
obj.display()"""

#2 types of methods
#instance method
#static method

class myclass():
    def myfun(self):
        print("this is instance method")
    @staticmethod   
    def display(self,name):
        print(self,name) # self also take one argument
        
obj=myclass()
obj.myfun()
obj.display("asha","hi")

myclass.display(10,20)#static method here we are calling through class not with object.

#global Variable
#class variable
#local variable

#self is all way representing class 
i,j=10,20 #global variable
class myclass:
    x,y=30,40 #class variable
    def add(self,a,b): # local variable
        print(a+b)
        print(self.x+self.y) #class variable
        print(i+j)
obj=myclass()
obj.add(50,20)
"""variable name are same"""
i,j=10,20 #global variable
class myclass:
    i,j=30,40 #class variable
    def add(self,i,j): # local variable
        print(i+j)
        print(self.i+self.j) #class variable
        print(globals()["i"]+globals()["j"])
obj=myclass()
obj.add(50,20)

#constructor method
"""method & constructor
method--->give any name 
          method can take arguments/Parameter
          we use object to call the method
constructor--->__init__(self)
              can take arguments/Parameter"""
class Myclass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("hello")
    def m2(self,x,y):
        return(x+y)
mc=Myclass()
mc.m1()
print(mc.m2(5,7)) 

#taking parameter in constructor
class Myclass:
    name="asha" #class variable
    def __init__(self,name):
        print(name) #class variable
        print(self.name) # local variable
mc1=Myclass("reetu")   

class emp:
    def __init__(self,eid,name,sal):
        self.eid=eid #eid is local variable converting into class variables 
        self.name=name
        self.sal=sal
    def display(self):
        print(self.eid,self.name,self.sal)
mc2=emp(123,"asjaslk",50000)
mc2.display() 
  

#__str__    return the string data
class emp:
    def __init__(self,eid,name,sal):
        self.eid=eid #eid is local variable converting into class variables 
        self.name=name
        self.sal=sal
    def __str__(self):
        return(self.name)
mc2=emp(123,"asjaslk",50000)
print(mc2)
   