'''
Created on 25-Jan-2023

@author: Asha
'''
"""expection handling
when user is giving invalid input so that is expection handling reset ofthe statement will not excuite"""
"""expection is a event which will cause program termination"""
"""multiple except block can be written by using name can be written for error,name,zerodivion"""

"""3 type of expection
1.try,expect,else,finally"""
#expect will occur when error 
#else no error
#finally if error no error finally stataemnt will excute 
"""example1"""
a=int(input("enter the number:"))
b=int(input("enter the number:"))
try:
    print(c)
except:
     print("expection occur")
     print("program is write")
     print("program is wrong")
     
"""example 2"""     
a=int(input("enter the number:"))
b=int(input("enter the number:"))
try:
    print(a/b)#1/0 ZeroDivisionError: division by zero
except ZeroDivisionError:
    
    print("expection occur")
print("program is write")
print("program is wrong")

#example 3 try,expect,else,finally
try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a/b)
except NameError:
     print(" NameError expection occur")
except ZeroDivisionError:
    print("expection error")
except:
    print("expection handled")        
    print("program is write")
    print("program is wrong")
else:    
    print("no expection occured")
finally:
    print("always execut!!!")    
#user diffent expection
def prime(num):
    if num<0:
        raise ValueError("only interger allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
num=-1 #user giving input
try:
    prime(num)
except ValueError:  
    print("value error")  
    
"""Calculation"""
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1/num2)
print("please select the operstion:")
choice=int(input("enter the choice(1/2/3/4):"))
try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
except:
    print("error occured")
else:
    print("value is given correct")
finally:
   print("program is done!!!")
      
if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
if choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))
if choice==3:
    print(num1,"*",num2,"=",mul(num1,num2))
if choice==4:
     print(num1,"/",num2,"=",div(num1,num2))
           
    