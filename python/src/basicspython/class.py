'''
Created on 16-Jan-2023

@author: Asha
'''
class Employee:
    id=10
    name="Harish"
    def display(self): 
        print(self.id,self.name)
emp=Employee()
emp1=Employee()
emp.display();
emp1.display();   

class Employee5:
    def display(self,id,name):
        print(id,name)
emp = Employee5()      
emp1 = Employee5()
emp3=Employee5()
emp.display(1,"swami");
emp1.display(2,"vinay");
emp3.display(3,"Sharan");