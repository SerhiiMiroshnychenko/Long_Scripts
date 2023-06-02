#read file in one-line
[line.strip() for line in open(filename)]

map(lambda x:x**2, [i for i in range(3)]) 
# <map object at 0x105558a90>

filter(lambda x: x % 2 == 0, [1, 2, 3])
# <filter object at 0x1056093d0>

from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3])
# 6

