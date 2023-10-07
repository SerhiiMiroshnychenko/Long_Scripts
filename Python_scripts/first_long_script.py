"""Numpy array Assigning Single Values"""

import numpy as np

# array[row, column]
# remember indexing starts from zero.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums_arr = np.array(nums)
nums_arr[3] = 33
print(nums_arr)

tens = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90]

nums_and_tens = nums + tens
nums_and_tens_arr = np.array(nums_and_tens)
nums_and_tens_arr = nums_and_tens_arr.reshape((2,10))
print(nums_and_tens_arr)
nums_and_tens_arr[0, 3] = 333
print(nums_and_tens_arr[1, 4])
nums_and_tens_arr[1, 4] = 444
print(nums_and_tens_arr)

nums_and_tens_arr[0,:] = 14
print(nums_and_tens_arr)

nums_and_tens_arr[:5, :5] = 0
print(nums_and_tens_arr)

nums_and_tens_arr = nums_and_tens_arr.reshape((2,2,5))

print('\nNew arr: ', nums_and_tens_arr)

print(nums_and_tens_arr.shape)


nums_and_tens_arr[:,:, 0] = [[111, 222], [333, 444]]
print('\nArr55: ', nums_and_tens_arr)

nums_and_tens_arr[:, :, :2] = 777
print('', )


# Python Program to Flatten a Nested List

# Example 1: Using List Comprehension

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)

# Example 2: Using Nested for Loops (non pythonic way)

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)

# Example 3: Using itertools package

import itertools

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)

# Example 4: Using sum()

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = sum(my_list, [])
print(flat_list)

# Example 5: Using lambda and reduce()

from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x+y, my_list))

# Подивитися вихідний код

import inspect
from queue import Queue

print(inspect.getsource(Queue))

# One line if statement:

if a > b: print("a is greater than b")


# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")


# Loops through a list of words and returns a new list containing all elements that are present on the given string

#: sample list
list_ = ['hello', 'welcome', 'guest', 'show']
#: sample string
sentence = "Hello world! Im here to show you a word filter"

#: print all words in list that are present in sentence
print([word for word in list_ if
       word in ("".join(word for word in sentence.lower() if word.isalpha() or word.isnumeric() or word == " ")).split(
           " ")])

# Finding all subsets of a set in one line
from itertools import combinations

# list of all subsets of
# length r (r = 2 in this example)
print(list(combinations([1, 2, 3, 4], 2)))

# Read file in python and input it to a list. 
file = open('gfg.txt', 'r')
lis = []
for each in file:
    # removing '\n' from the end of the string
    a = each[:-1]
    lis.append(a)
file.close()
# or
lis = [line.strip() for line in open('gfg.txt', 'r')]

# Finding the factorial

n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

import math

n = 5
print(math.factorial(n))

n = 5
# one liner code for half pyramid pattern
print('\n'.join('* ' * i for i in range(1, n + 1)))

# To input a 2-D matrix(When the entries are given row-wise): The most naive method that comes in mind while taking a input for 2-D matrix is given below. 

# Input for row and column
R = int(input())
C = int(input())
matrix = []

# for loop for row entries
for i in range(R):
    a = []
    # for loop for column entries
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

# Input for row and column
R = int(input())
C = int(input())

# Using list comprehension for input
matrix = [[int(input()) for x in range(C)] for y in range(R)]

# To input space separated integers in a list
lis = list(map(int, input().split()))

with open('D:/Python/LongScripts/JS_scripts/first-long-script.js') as file:
    lines = {f"Line {count_ + 1}: " + line.strip() for count_, line in enumerate(file)}

# Discouraged
with open('D:/Python/LongScripts/JS_scripts/first-long-script.js') as file: lines = [
    f"Line {count_ + 1}: " + line.strip() for count_, line in enumerate(file)]

# Traditional way
lines = []
with open('D:/Python/LongScripts/JS_scripts/first-long-script.js') as file:
    for count_, line in enumerate(file):
        lines.append(f"Line {count_ + 1}: " + line.strip())

# Pythonic way
with open('D:/Python/LongScripts/JS_scripts/first-long-script.js') as file:
    lines = [f"Line {count + 1}: " + line.strip() for count, line in enumerate(file)]

my_set = set(count_ ** x for x in range(count_))
print(my_set)
# Shows: {1, 4, 16, 64}


my_set = set(range(count_))
my_tuple = tuple(range(count_))

# Result
print(my_set)
# Shows: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_tuple)
# Shows: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


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
