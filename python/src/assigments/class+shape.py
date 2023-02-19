'''
Created on 22-Jan-2023

@author: Asha
'''
"""Create a class named ‘Shape’ with a method to print “This is this shape”. 
Then create two others classes named ‘Rectangle’, ‘Circle’ 
inheriting the shape class, both having the method to print “This is rectangular shape” and “This is circular shape” respectively"""
#multiple two parent 1 child
class shape:
    def abc(self):
        print("This is this shape")
class rectangle():
    def efg(self):
        print("This is rectangular shape!!!")        
class circle(shape,rectangle):
    def hij(self):
        print("This is circular shape!!!")
a2=circle()
a2.abc() 
a2.efg()      
a2.hij()        