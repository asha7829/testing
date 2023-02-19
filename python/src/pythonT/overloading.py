'''
Created on 18-Jan-2023

@author: Asha
'''
# First product method.
# Takes two argument and print their
# product
 
class prod:
    def product(self,a,b):
        p = a * b
        print(p)
 
# Second product method
# Takes three argument and print their
# product
    def product(self,a,b,c):
      d = a * b * c
      print(d)
 
# Uncommenting the below line shows an error
#product(4, 5)
 
 
# This line will call the second product method
p1=prod()
#p1.product(4,5)
p1.product(4,5,6)

