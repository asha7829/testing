'''
Created on 21-Jan-2023

@author: Asha
'''
"""Create a class to print a integer and a character with two methods having the same name but different sequence of the integer and the character parameters.
For example, if the parameter of the first method are of the form (int n, char c), then that of the second method will be of the form (char c, int n)."""

class asha:
    def first(self,ch,n):
        self.ch=ch
        self.n=n
        if (ch.isalpha()):
            if(n<=10):
                print("sequence of integer and charater:","".join,ch,n)  
    def first(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        if (a==1):
            print("its right number")
        else:
            print("not equal")   
        if (b<=10):
            print("its an interger")
        if (c.isalpha()):
            print("its a char ")          
                         
a=asha()
#a.first("anu",2)
a.first(0,2,"reetu")


""" Method Overloading:
Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 
These methods are called overloaded methods and this is called method overloading.  """

"""def product(a, b):
    p = a * b
    print(p)
 
# Second product method
# Takes three argument and print their
# product
 
 
def product(a, b, c):
    p = a * b*c
    print(p)
 
# Uncommenting the below line shows an error
product(4, 5)
 
 
# This line will call the second product method
#product(4, 5, 5)"""
      
"""class asha:
    def first(self,ch,n):
        self.ch=ch
        self.n=n
        if (ch.isalpha()):
            if(n<=10):
                print("sequence of integer and charater:","".join,ch,n)  
    def first(self,n,c):
        self.n=n
        self.c=c  
        if (n<=10):
            print("its an interger")
        if (c.isalpha()):
            print("its a char ")          
                         
a=asha()
#a.first("anu",2)
a.first(4,"reetu")"""
