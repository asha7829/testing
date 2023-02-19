'''
Created on 26-Jan-2023

@author: Asha
'''
import Day9
Day9.animal()
Day9.bird()

import module2
module2.animal()
module2.bird()

from Day9 import *
animal()
bird()

from module2 import *
animal()
bird()

#using class and function approch1
import Day9
import module2

obj1=Day9.Animal()
obj1.display()

obj2=module2.bird()
obj2.display()

#approch 2
from Day9 import Animal
from module2 import bird

obj1=Animal()
obj1.display()

obj2=bird()
obj2.display()
