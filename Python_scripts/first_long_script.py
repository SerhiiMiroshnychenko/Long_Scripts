# List with descending values and negative values
my_list = list(range(5, -5, -1))
print(my_list)
# Shows: [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]


my_tuple = (1, 2) * 5
print(my_tuple)
# Shows: (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)


size = 10
 
# Traditional way
my_list = []
for i in range(size):
    my_list.append(0)
 
# Pythonic way
my_list = [0] * size
 
# Result
print(my_list)
# Shows: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Pythonic way
a, b, c, d = 1, "ok", True, ["i", "j"]
a, b, c, d = c, a, d, b
 
# Result
print(a, b, c, d)
# Shows: True 1 ["i", "j"] ok


x = 3
 
# Traditional way
if x % 2 == 1:
result = f"{x} is odd"
else:
    result = f"{x} is even"
 
# Pythonic way
result = f"{x} " + ("is odd" if x % 2 == 1 else "is even")
 
# Result
print(result)
# Shows: 3 is odd


# Найчастіший елемент у списку
lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
frequent = max(set(lst), key=lst.count)
print(frequent)

# read file in one-line
[line.strip() for line in open('D:/Python/LongScripts/JS_scripts/first-long-script.js')]

map(lambda x: x ** 2, list(range(3)))
# <map object at 0x105558a90>

filter(lambda x: x % 2 == 0, [1, 2, 3])
# <filter object at 0x1056093d0>

from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3])
# 6

# one-liner
print(*range(1, 5))  # 1 2 3 4

# without walrus
import re

discount = 0.0
if mo := re.search(r'(\d+)% discount', "10% discount"):
    discount = float(mo[1]) / 100.0
# with walrus
discount = 0.0
if (mo := re.search(r'(\d+)% discount', "10% discount")):
    discount = float(mo[1]) / 100.0

# without walrus
f = open("D:/Python/LongScripts/JS_scripts/first-long-script.js")
line = f.readline()
while line != '':
    print(line)
    line = f.readline()
# with walrus
f = open("D:/Python/LongScripts/JS_scripts/first-long-script.js")
while (line := f.readline()) != '':
    print(line)

# Fibonacci algorithm
fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)

# quick sort, a famous sorting algorithm
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
q([])
