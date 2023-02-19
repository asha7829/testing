'''
Created on 26-Jan-2023

@author: Asha
'''

#approch1
import Day9
Day9.add(3,2)
Day9.mul(3,2)

#approch2
from Day9 import add,mul
add(9,4)
mul(9,4)

#approch3
from Day9 import * #this will include all functions and class
add(9,4)
mul(9,4)

def animal():
    print("animal cant fly")
def bird():
    print("bird color is white")
    
class bird:
    def display(self):
        print("bird can fly")