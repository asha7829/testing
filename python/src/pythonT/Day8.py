'''
Created on 26-Jan-2023

@author: Asha
'''
"""object based programming languages support class,object,method,constructor"""
"""object oriented programing language support class,object,method,cons,inhertance"""
#inhertance
"""aquiring all the attribute(variable) and behaviour(method) from one class to another class is called inhertancde"""
"""class A: ---->a,b,c m1(),m2() ----->A is parent of B class  (base class/super class)
class B(A):--->x,y,z m3()---->B is child class of A class    (sub class/derived class)"""

"""class loan:-->parent class 30 methods return 
class personal (loan):--->child class 20 methods return 
we are using inhertance concept because resubility of code will be done from child class """

"""objective of inhertance
1)code re-Usability
2)avoid duplication

4 types of inhertance
single,multi-level,heirarchy,multiple"""

"""single
one parent one child"""

"""multi-level
multi child """
"""heriarchy
one parent one child two child"""
"""multiple
two parent one child"""

#example1 single 
"""class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A):
    def m2(self):
        print("this is m2 method from class B")
obj=B()
obj.m1()
obj.m2()  """
"""
#example2 single
class A:
    x,y=10,20 #class having 2 variable and method 
    def m1(self):
        print(self.x + self.y)
class B(A):
    x,y=10,20 #class having 2 variable and method 
    def m2(self):
        print(self.x * self.y)        
        
obj=B()
obj.m1()
obj.m2()

#example2 multi-level
class A:
    x,y=10,20 #class having 2 variable and method 
    def m1(self):
        print(self.x + self.y)
class B(A):
    x,y=10,20 #class having 2 variable and method 
    def m2(self):
        print(self.x * self.y)        
class C(B):
    x,y=20,10
    def m3(self):
        print(self.x - self.y)
        
obj=C()
obj.m1()
obj.m2()
obj.m3()
 
#example2 heriachly
class A:
    x,y=10,20 #class having 2 variable and method 
    def m1(self):
        print(self.x + self.y)
class B(A):
    x,y=10,20 #class having 2 variable and method 
    def m2(self):
        print(self.x * self.y)        
class C(A):
    x,y=20,10
    def m3(self):
        print(self.x - self.y)
        
obj=B()
obj.m2()
obj.m1()   

 #example2 multiple
class A:
    x,y=10,20 #class having 2 variable and method 
    def m1(self):
        print(self.x + self.y)
class B:
    x,y=10,20 #class having 2 variable and method 
    def m2(self):
        print(self.x * self.y)        
class C(A,B):
    x,y=20,10
    def m3(self):
        print(self.x - self.y)
        
obj=C()
obj.m3()
obj.m1() 
obj.m2() """

""""differnt cenero(OVERRIDDING)"""  #super keyword used for invoke the parent class of method through child class

class A:
    def m1(self):
        print("this is m1 class A")
class B(A):
    def m1(self):
        print("this is m1 class B")
        super().m1()
                 
obj=B()
obj.m1()

class A:
    a,b=10,20
class B(A):
    X,Y=20,30
    def m(self,c,b):
        print(c+b)#local variable dont use self
        print(self.X * self.Y)#class variable using self 
        print(self.a -self.b)#class variable using self
obj=B()
obj.m(200,7)
        
#overridding variable
class parent:
    name="asha"
class child(parent):
    name="reetu"
    def test(self):
        print(super().name)
obj=child()
print(obj.name)        
obj.test()

"""polymorphism mean many using overloding concept (one thing shape--->many forms -->circle,rec,sq) 
shape-->circle,rec,sq"""

#example overloading concept
class human:
    def ggkk(self,name=None):
        if name is not None:
            print("hello"+name)
        else:
         
             print("hello")
                
obj=human()
obj.ggkk("asha")

class cal:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
obj=cal()
obj.add()        
obj.add(19,50)
obj.add(45,2,3)