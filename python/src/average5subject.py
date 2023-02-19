'''
Created on 09-Jan-2023

@author: Asha
'''
eng=int(input("enter the eng marks:"))
mat=int(input("enter the mat marks:"))
soc=int(input("enter the soc marks:"))
sci=int(input("enter the sci marks:"))
com=int(input("enter the com marks:"))
total=eng+mat+soc+sci+com
print("total subject marks",total)
avg=total/5
if avg>90:
    print("grade A congraultion")
elif avg>70 and avg<80:  
    print("grade B ")
elif avg<=50 and avg>60:
    print("grade c")      
else:
    print("exit")    