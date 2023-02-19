'''
Created on 22-Jan-2023

@author: Asha
'''
"""Create an Interface class ‘Bank’ with an abstract method ‘getBalance’. 
$100 , $150 and $200 are deposited in banks A, B and C respectively. ‘BankA’, ‘BankB’ and ‘BankC’ are subclasses of class ‘Bank’, each having a method named ‘getBalance’.
Call this method by creating an object of each of the three classes."""
from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,value):
        self.value=value    
    @abstractmethod
    def getbalance(self):
        pass
class BankA(Bank):
    def getbalance(self):
        print("amount got deposited BankA",self.value)
class BankB(Bank):
    def getbalance(self):
        print("amount got deposited BankB",self.value) 
class BankC(Bank):
    def getbalance(self):
        print("amount got deposited BankC",self.value)                 
        
a=BankA(100)
a.getbalance() 
b=BankB(150)
b.getbalance()  
c=BankC(200)
c.getbalance()
    