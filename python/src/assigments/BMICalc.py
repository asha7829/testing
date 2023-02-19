'''
Created on 14-Jan-2023

@author: Asha
'''
#BMI(body mass index)
"""height=float(input("enter the height:"))
weight=int(input("enter the weight:"))
BMI=weight/height**2
print(BMI)
if BMI<18.5:
    print("underweight")
if BMI>18.5 and BMI>25:
    print("normal") 
if BMI>=20 and BMI<30:
    print("overweight")
if BMI>=30:
    print("obesity")"""        
 
def main():
    he=float(input("enter the height:"))
    we=int(input("enter the weight:"))
    bmi=we/(he*he)
    print("your body mass",bmi)  
    if bmi <= 18.5:
        print("underweight")    
    elif bmi <= 25:
        print("normal") 
    elif bmi <= 30:
        print("overweight")
main()
 
       






           
