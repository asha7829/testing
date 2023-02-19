#all prime numbers.
"""f=int(input("enter the first number:"))
l=int(input("enter the end number:"))
for num in range(f,l+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)  """  
            
#sum using for range
"""for i in range (10):
    print(i)     
    
print(sum(range(10)))  """          


"""sum=0
for i in range(10):
    print(i)
    sum+=i
print(sum)"""

"""list=["apple","babana","orange","mango","kiwi"]
print("what you want to serach:")
n=input()
for lis in list:
    print(lis)
    if lis==n:
        print("we found")
        break
    print("end of the loop iteration")"""
    
            
for i in range(6):
    for j in range(i+1):
        print(j,end=" ")
    print("\n")
    
       
    
rows = int(input("Enter number of rows: "))

ascii_value = 64

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")    
    
              