'''
Created on 24-Jan-2023

@author: Asha
'''
"string is datatype which enclosed with double couts and single couts"
"index start from 0"
name="harry"
print(name[0])
"looping throught strings for loop"
for i in name:
    print(i)
"string silicing operator " 
print(name[0:3]) #har
print(name[:4])#harr
print(name[-3:-1])#rr len name 5-3=2 and 5-1=4[2:4]

print(name[-4:-2])#ar

import time
a=time.strftime('%h:%m:%s')
print(a)
