'''
Created on 07-Jan-2023

@author: Asha
'''
try:
   ah = open("tes", "r")
   ah.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
  
   
try:   
   ah = open("tes", "w")
   ah.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
ah.close()



def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

#Handling run-time error: division by zero


