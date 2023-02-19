'''
Created on 25-Jan-2023

@author: Asha
'''
"""Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare."""
class Vehicle:
    def __init__(self,capacity):
        self.capacity = capacity
        print("seating capacity","=",self.capacity)
class bus(Vehicle):
    def amount(self,fare):
        self.fare=fare
        finalamount=self.fare+.1+self.capacity*100
        print("so total fare:","=",finalamount)
a=bus(60)
a.amount(100)



                
