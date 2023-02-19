'''
Created on 11-Jan-2023

@author: Asha
'''
list=[]# interger,string charater,starting with 0 mutable 
print(list)
#we can use slicing operater,reverse,pop,ascessingindex,sort,append,remove,count,extend
#for,max,min,len,sum,+,in ,not in,clear,del

list1=[1,3,4,2]
list2=[7,1,3,5]
list1,list2=list2,list1 #swapping the list
print(list1,list2)

ln=list1+list2 #conctent
print(ln)
print(list1[3])#index value
print(len(list1))

#max
#n=[3,67,23,12]
#print(max(n))
#print(min(n))

def minimum(a, b):
      
    if a <= b:
        return a
    else:
        return b
      
# Driver code
a = 2
b = 4
print(minimum(a, b))

def max(a,b):
    if a>=b:
        return a
    else:
        return b
a=4
b=2
print(max(a,b))  

list=["greek","asha","reetu"]
if ("asha" in list):
    print("yes")
else:
    print("not")    
    
if ("reetu" not in list): 
     print("yes")
else:
    print("not")
            
    
            