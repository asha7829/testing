'''
Created on 16-Jan-2023

@author: Asha
'''
import random
import array
maxlen=12
digit=0,1,2,3,4,5,6,7,8,9
locase_alp='a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'
uppercase_alp='A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'
symbol = '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<'
comblist=digit+locase_alp+uppercase_alp+symbol
# randomly select at least one character from each character set above
a=random.choice(digit)
b=random.choice(locase_alp)
c=random.choice(uppercase_alp)
d=random.choice(symbol)
temp_pass = a + b + c + d
for x in range(maxlen-4):
    temp_pass=temp_pass+random.choice(comblist)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)
    password=""
    for x in temp_pass_list:
        ps=ps+x
    print(ps) 
    
import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+_-{}[].,/\<>"
maxlength=int(input("enter the password length:"))
a = "".join(random.sample(password,maxlength))
print("your password:",a)