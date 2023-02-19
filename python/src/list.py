'''
Created on 11-Jan-2023

@author: Asha
'''
#list=[23,3,5,1,3]
#list.sort()
#print(list,"assending order")

#reverse=True will sort the list descending order.
#list.sort(reverse=True)
#print(list,"descending order")

"""list=[23,3,5,1,3] #5 elements
for i in range (0,len(list)):#0,4
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
            print(list) """

   
#assending order 
"""list=[78,67,4,34,27]
for i in range (0,5):
    for j in range (i+1,5):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
            print(list)"""
#descending order           
list=[78,67,4,34,27]
for i in range (0,5):
    for j in range (i+1,5):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
            print(list)           
            
            
            
