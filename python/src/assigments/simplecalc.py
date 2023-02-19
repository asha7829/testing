'''
Created on 17-Jan-2023

@author: Asha
'''
#simple calc
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("selector operator:\n"\
      "1.Add\n"\
      "2.sub\n"\
      "3.mul\n"\
      "4.div\n")
slecet=int(input("select the operations from 1,2,3,4:"))
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
if slecet==1:
    print(num1,"+",num2,"=",add(num1, num2))
elif slecet==2:
    print(num1,"-",num2,"=",sub(num1, num2))  
elif slecet==3:
    print(num1,"*",num2,"=",mul(num1, num2)) 
elif slecet==4:
    print(num1,"/",num2,"=",div(num1, num2))  
else:
    print("invalid input")
        


