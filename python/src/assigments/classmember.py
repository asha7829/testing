'''
Created on 22-Jan-2023

@author: Asha
'''
"""Create a class named ‘Member’ having the following.
Members:-
Data members
a-name
b-age
c-phone number
d-address
e-salary.
It also has a method named ‘printSalary’ which prints salary of the members.
Two classes ‘Employee’ and ‘Manager’ inherit the ‘Member’ class. 
The ‘Employee’ and ‘Manager’ classes have data members ‘Specialization’ and ‘department’ restively. 
Now assign name, age, phone number, address and salary to an employee and a manager by making an object of both these classes and print the same."""
class Member:
      def display(self,name,age,ph,addr):
          print(name,age,ph,addr)
      def salary(self,salary):  
          print(salary)            
class Employee(Member):
    def abc(self,spec,dep,name,age,ph,addr,sa):
        print(spec,dep,name,age,ph,addr,sa)
class Manager(Member):  
    def ghi(self,spec,dep,name,age,ph,addr,sa):
        print(spec,dep,name,age,ph,addr,sa)             
          
a=Manager()
a.ghi("doct","ear","asha",34,6789,"fjku",34)
a.display("reetu", 67, 70097, "fkygfda")
a.salary(67)

b=Employee()
b.abc("tec", "sci", "aadsd", 79, 56756, "ashfkef", 78)
b.display("sat", 56, 878, "hjsds")
b.salary(78)



        