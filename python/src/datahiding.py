'''
Created on 10-Jan-2023

@author: Asha
'''
class Solution:
    __privateCounter = 0
 
    def sum(self):
        self.__privateCounter += 1
        print(self.__privateCounter)
 
 
count = Solution()
count.sum()
count.sum()
count.sum()
 
# Here it will show error because it unable
# to access private member
#print(count.__privateCount)

