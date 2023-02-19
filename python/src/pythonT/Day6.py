'''
Created on 28-Jan-2023

@author: Asha
'''
#Functions
"""function means set of statement which will perform a task ""once you create a function we call any number of time.resubility"""
#1.function declration/Creation
#2.calling the function/invoking function

#example1:
def myfun():
    print("hello")#function creation
    
myfun()#calling function

#example2
def myfun(name):
    print("hello",name)#creation of function
myfun("asha")   #calling the function

#example3
def cal(a,b):
    return(a+b)#creation of function
print(cal(10,20))#calling the function

#example4
def fun():
    return 
print(fun())

def fun():
    i=10  
print(fun())

"""variable means which store the data
2 types of Variable
global Variable
local Variable"""

#global variable which is outside the function can acess any where
#local variable which is inside the function  but in local we need to access inside the function

#example1:
global_var=10 #global variable can call from inside the function and outside

def func():
    local_var=20# local variable can access inside the function
    print(local_var)
    print(global_var)
func()
print(global_var) 

#example2:
xy=100 #global variable

def func():
   # global xy=100# invaild statement
    global xy #inside the function use global keyword
    xy=200 
    print(xy)
    
#func()
print(xy)

"""2 types of arguments/parameter can be passed in function"""
#1.positional arguments
#2.keyword arguments

#example1:
def func(i,j):
    print(i,j)
    
func(10,20)#postional arguments
func(j=20,i=10)#keyword arguments

#example2 defauklt value passing
def fun(i,j=50):
    print(i,j)
    
fun(10)#postional arguments





