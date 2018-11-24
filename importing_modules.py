'''
import math
print(math.pi)
print(math.floor(math.pi))
'''

from math import *
print(pi)

import random

print('Liczba całkowita randomowa od 1 do 100: ', random.randint(1,100))

print('Liczba całkowita randomowa inaczej od 1 do 100: ', random.choice(range(1,100)))
print(random.randrange(1,100))

list = [1,2,3,43,534,543,6,3224,432,42,3]
random.shuffle(list)
print(list)

print('Random float: ', random.random())
print('---------------------------- \n')

#for i in range(32,127):
 #   print(i, chr(i))

import random

ints = range(33,127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print('Password is: ', password)












    
