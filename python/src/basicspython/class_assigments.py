'''
Created on 16-Jan-2023

@author: Asha
'''
class area:
    pi=3.14
    r=float(input("Enter radious to find area: "))
    circle=pi*r*r
    print("the area of the circle is")
    def display(self):
        print(self.circle)
a=area()
a.display();

class rectangle:
    l=float(input("Enter length to find area of rectangle: "))
    b=float(input("Enter breadth to find area of rectangle: "))
    rect=l*b
    print("the area of rectangle is")
    def display(self):
        print(self.rect)
rect=rectangle()
rect.display();

class average:
    print("enter 5 numbers to get average")
    n1=int(input("Enter a number: "))
    n2=int(input("Enter a number: "))
    n3=int(input("Enter a number: "))
    n4=int(input("Enter a number: "))
    n5=int(input("Enter a number: "))
    avg=(n1+n2+n3+n4+n5)/ 5
    print("the average of 5 subjects are")
    def display(self):
        print(self.avg)
avg=average()
avg.display();

class grade:
    def display(self):
        avg=float(input("Enter marks to find grade: "))
        if(avg>=85) and (avg<=100):
            print("distinction")
        elif(avg>=60) and (avg<=80):
            print("first class")
        elif(avg>=50) and (avg<=60):
            print("second class")
        elif(avg>=35)and(avg<=40):
            print("third class")
        elif(avg>100):
            print("invalid")
        else:
            print("fail")
gd = grade()      
gd.display();


class leap:
    num = int(input("Enter a year to find leap or not: "))
    if(num%4==0):
        print("leap year")
    else:
        print("not a leap year")
    def display(self):
        print(self.num)
b=leap()
b.display();

class even_odd:
    num = int(input("Enter a number to check even or odd: "))
    if(num%2==0):
        print("even number")
    else:
        print("odd number")
    def display(self):
            print(self.num)
even=even_odd()
even.display();

class simple_interest:
    print("simple interest")
    p=float(input("Enter a number for p: "))
    t=float(input("Enter a number for t: "))
    r=float(input("Enter a number for r: "))
    interest=(p*t*r)/100
    def display(self):
        print("the simple interest is")
        print(self.interest)
simple=simple_interest()
simple.display();
