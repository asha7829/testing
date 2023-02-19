'''
Created on 20-Jan-2023

@author: Asha
'''
def roman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
    thousand = m[(num // 1000)//1000]
    hunderd = c[(num % 1000)//100]
    tens = x[(num % 100)//10]
    ones = i[(num % 10)]
    ans=(thousand+hunderd+tens+ones)
    return(ans)
    

number = 444
print(roman(number))
  