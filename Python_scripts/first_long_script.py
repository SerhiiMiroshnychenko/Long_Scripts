"""
My Square Iterator
"""

class MySquareIterator:
  def __init__(self, from_, to_, step_=1):
    self.ind = from_
    self.start = from_
    self.to = to_
    self.step = step_

  def __iter__(self):
    return self

  def __next__(self):
    if self.ind > self.to:
      raise StopIteration
    val = self.ind ** 2
    self.ind += self.step
    return val

  def __str__(self):
    return f'Iterator(start:{self.start}, end:{self.to}, step:{self.step})'
 

c = MySquareIterator(1,10,2)
for i in c:
  print(i)

try:
 next(c)
except Exception as e:
  print(e.__class__, e)

print(c)


"""
my_squares_generator
"""

def my_squares_generator(f, t, s=1):
   for i in range(f, t+1, s):
      yield i ** 2

c = my_squares_generator(1, 10, 2)

print (c)
print (*c, sep=' ➡️ ')


s1 = (i**2 for i in range(10))
s2 = [i**2 for i in range(10)]

print (*s1, sep=' ➡️ ')
print (*s2, sep=' ➡️ ')



"""
wrap from functools
"""

from functools import wraps
 
def stop_words(words: list):
  def stop_words_decor(func):
    @wrapper(func):
    def wrap(*args, **kwargs):
      result = func(*args, **kwargs)
      for word in words:
        result = result.replace(word, '*')
      return result
    return wrap
  return stop_words_decor
 
 
 
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
     print(f"{name} drinks pepsi in his brand new BMW!")
     return f"{name} drinks pepsi in his brand new BMW!"



"""
Defended Vector Class
"""

class DefendedVector:
  def __init__(self, v):
    self.__v = v

  def __enter__(self):
    self.temp = self.__v[:]
    return self.temp

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is None:
      self.__v[:] = self.temp
    else:
      print(exc_type, exc_val, exc_tb, sep='\n')
    return True

v1 = [1,2,3]
v2 = [2,3]
v3 = [2,3,4]

vect = DefendedVector(v1)
print('vect=',vect._DefendedVector__v)


with vect as v:
  for i, el in enumerate (v):
    v[i] += v2[i]
    print(v)
    

print('v1=',v1)
print('vect=',vect._DefendedVector__v)

with vect as v:
  for i, el in enumerate (v):
    v[i] += v3[i]
    print(v)

print('v1=',v1)
print('vect=',vect._DefendedVector__v)


"""
Type Decorator Class
"""

class TypeDecorators:

  def to_int(func):
    def inner(*args):
      return int(func(*args))
    return inner

  @to_int
  def __call__(self, )
    

@TypeDecorators.to_int
def add_func(a, b):
  return a + b

x = add_func
print(x)

"""
Class Decorator
"""

import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def show(self):
      print(self.num_calls)
      

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")

say_whee()
say_whee()
print(say_whee.num_calls)
say_whee.show()



"""
Generator 
"""

def sequence(end):
    num = 0
    while True:
        yield num
        try:
           num += 1
        except StopIteration:
           num = 0
           print (num)
           return 

s = sequence(10)
print(*s)
print(*s)


"""
Context manager
"""

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')

with File('demo.txt', 'r') as opened_file:
    print(opened_file.read())


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()



"""
Context manager as a generator
"""

from contextlib import contextmanager

@contextmanager
def open_file(name, v):
    f = open(name, v)
    try:
        yield f
    except Exception as e:
      print(e.__class__, e)
    finally:
        f.close()

with open_file('some_file.txt', 'w') as f:
    f.write('hola!')

      
with open_file('some_file.txt', 'r') as f:
    print(f.read())


"""
Question 0
"""

x = 5
print (x << 2)


"""
Coma equal 
"""

x = 1
y = [2]

x ,= y

print(x)

x = 1
y = [2, 3]

x,a ,= y

print(x)
print(a)


"""
Open class
"""

class Open:
  def __init__(self, name, mode):
    self.name = name
    self.mode = mode
    self.file = None

  def __enter__(self):
    if self.mode != 'x':
      try:
        self.file = open(self.name, 'r')
        self.copy_file = self.file.read()
        self.file.close()
      except BaseException as e:
        print(e.__class__, e)
    self.file = open(self.name, self.mode)
    return self.file

  def __exit__(self, er, val, tb):
     if er:
       print(er, val, tb)
       return True
     else:
       return None
     if self.file and not self.file.closed:
       self.file.close()
       
try:
  with Open('text.txt', 'r') as f:
    print(f.read())
except BaseException as e:
  print(e.__class__, e)


"""
Task with is
"""

a = 5.
b = 5. ** 2
b /= a
print (a is b)


"""
Linear search
"""
# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1
 
 
def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
 
 
# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)
 
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)


"""
Sentinel linear search 
"""
# Python3 implementation of the approach
# Function to search key in the given array
 
 
def sentinelSearch(arr, n, key):
 
    # Last element of the array
    last = arr[n - 1]
 
    # Element to be searched is
    # placed at the last index
    arr[n - 1] = key
    i = 0
 
    while (arr[i] != key):
        i += 1
 
    # Put the last element back
    arr[n - 1] = last
 
    if ((i < n - 1) or (arr[n - 1] == key)):
        print(key, "is present at index", i)
    else:
        print("Element Not found")
 
 
# Driver code
arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
n = len(arr)
key = 180
 
sentinelSearch(arr, n, key)


"""
Recursive binary search 
"""

# Python3 Program for recursive binary search.
 
# Returns index of x in arr if present, else -1
 
 
def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1
 
 
# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


"""
Iterative Binary Search
"""

#Another Iterative Approach to Binary Search

def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1
 
    # This below check covers all cases, so need to check
    # for mid=lo-(hi-lo)/2
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
 
    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")
 
 
if __name__ == '__main__':
    v = [1, 3, 4, 5, 6]
 
    To_Find = 1
    binarySearch(v, To_Find)
 
    To_Find = 6
    binarySearch(v, To_Find)
 
    To_Find = 10
    binarySearch(v, To_Find)


"""
Iterable
"""

from collections.abc import Iterable

def unpack(array: list[int]) -> list[int]:
    for elem in array:
        try:
            unpack(elem)
        except:
            print(elem)
            yield elem          

def flat_list(array: list[int]) -> Iterable[int]:
    result = []
    for i in unpack(array):
        result.append(i)
    return result


list(flat_list([-1, [1, [-2], 1], -1]))


"""
Try-except
"""

try:
  """Code"""
except:
  print("Hello!")


"""
Two Sum
"""

def two_sum(numbers: list, target: int) -> list:
  for index, number in enumerate(numbers):
    print(f'{index=}: {number=}')
    for index, number in enumerate(numbers):
      if 
    

print(two_sum([2,7,11,15], 9))
#assert two_sum([2,7,11,15], 9) == [0,1]


"""
Disemvowel trolls
"""

def disemvowel_trolls(sentence: str) -> str:
  return ''.join(c for c in sentence if c.lower() not in 'euioa')



print(disemvowel_trolls("Delete all vowels!"))

print(disemvowel_trolls("123@#$&+&()%©®™✓[]aety"))

assert disemvowel_trolls("Delete all vowels!") == "Dlt ll vwls!"

assert disemvowel_trolls("QWERTY") == "QWRTY"


"""
D trolls
"""

def d_trolls(text: str) -> str:
  new_text = [c for c in text if c.lower() not in 'euioa']
  print(type(new_text))
  return new_text

print(d_trolls('Glory to Ukraine!'))

"""
Get order
"""

def get_order(order: str) -> str: 
  components = (
    'Burger', 
    'Fries', 
    'Chicken', 
    'Pizza', 
    'Sandwich', 
    'Onionrings', 
    'Milkshake', 
    'Coke'
    )
  fix_order = ''
  for word in components:
    if word.lower() in order:
      fix_order += f'{word} ' * order.count(word)
      
    #order=order.replace(word.lower(), f'{word} ')
    
  return order
  
if __name__ == "__main__": 
  print(get_order("burgersandwich")) # повертає "Burger Sandwich" 
  print(get_order("cokefriessandwichpizzaburger")) # повертає "Burger Fries Pizza Sandwich Coke" 
  print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich")) # повертає "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"


"""
Map
"""

def square(number):
     return number ** 2


numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)
print(list(squared))

qube = map(lambda x: x**3, numbers)
print(list(qube))

strings = map(str, numbers)
print(list(strings))

words = ["Welcome", "to", "Real", "Python"]

print(list(map(len, words)))


"""
Map for a few collections
"""

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))

first = [1, 2, 3, 4]
second = [10, 20, 30, 40, 50]
result = map(lambda x,y: x-y, second, first)

print(list(result))

print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))


"""
Map for string
"""

string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize, string_it)))

with_spaces = ["processing ", "  strings", "with   ", " map   "]

print(list(map(str.strip, with_spaces)))

with_dots = ["processing..", "...strings", "with....", "..map.."]

print(list(map(lambda s: s.strip("."), with_dots)))


"""
Map + re
"""

import re

def remove_punctuation(word):
     return re.sub(r'[!?.:;,"()-]', "", word)

print(remove_punctuation("...Python!"))

text = """Some people, when confronted with a problem, think
... "I know, I'll use regular expressions."
... Now they have two problems. Jamie Zawinski"""

words = text.split()
print(words)

print(list(map(remove_punctuation, words)))


"""
Map + math
"""

def powers(x):
     return x ** 2, x ** 3


numbers = [1, 2, 3, 4]

print(list(map(powers, numbers)))

import math

numbers = [1, 2, 3, 4, 5, 6, 7]

print(list(map(math.factorial, numbers)))

def to_float(number):
     try:
         return float(number.replace(",", "."))
     except ValueError:
         return float("nan")


print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"])))


"""
Map + filter
"""

import math

def is_positive(num):
     return num >= 0


def sanitized_sqrt(numbers):
     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
     return list(cleaned_iter)


print(sanitized_sqrt([25, 9, 81, -16, 0]))


"""
Starmap
"""

"""
intertools.starmap
==
def starmap(function, iterable):
    for args in iterable:
        yield function(*args)
"""

from itertools import starmap

print(list(starmap(pow, [(2, 7), (4, 3)])))

print(list(map(pow, (2, 7), (4, 3))))
print(list(map(pow, (2, 4), (7, 3))))


"""
Pythonic without Map
"""

# Generating a list with map
# list(map(function, iterable))

# Generating a list with a list comprehension
# [function(x) for x in iterable]


# Transformation function
def square(number):
     return number ** 2

numbers = [1, 2, 3, 4, 5, 6]

# Using map()
print(list(map(square, numbers)))

# Using a list comprehension
print([square(x) for x in numbers])

# Transformation function
def square(number):
     return number ** 2

numbers = [1, 2, 3, 4, 5, 6]

# Using map()
map_obj = map(square, numbers)
print(map_obj)


print(list(map_obj))

# Using a generator expression
gen_exp = (square(x) for x in numbers)
print(gen_exp)

print(list(gen_exp))

print(list(square(x) for x in numbers))


"""
Print numbers
"""

numbers =[1,2,3,4,5]
print(*numbers, sep='\n')


"""
Lambda abc
"""

a = lambda: print('Hello', end=' ')
b = lambda: print('Solo', end='')
c = lambda: print('Learn', end='!')

commands = a, b, c

for c in commands:
  c()


"""
Empty list to string
"""
empt = []
print(str(empt)+'[')


"""
Reduce-sum
"""

from functools import reduce

a,b,c = 1, 2, 3
x,y,z = 'a','b','c'

def add(*args):
  return reduce(lambda x,y: x+y, args)
  #return reduce(sum, args)

print(add(a,b,c))
print(add(x,y,z))

#print(sum([1,2,3]))
#print(sum(['a','b','c']))

nums = 1,2,3,4,5
chars = tuple('abcde')
print(chars)
print(sum(nums))
#print(sum(chars))
print(add(*chars))


"""
NumPy array sum
"""

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

cnt = 0
for height in heights:
    if height > 188:
        cnt +=1
print(cnt)

# Or simply just:
print(sum([(i>188) for i in heights]))

# Same with numpy
import numpy as np

heights_arr = np.array(heights)
print((heights_arr > 188).sum())

#======== Example ==========
a = [1,2,3,4,5,6]
b = np.array(a)

c = (b > 3)

# c = [False False False True True True]

print(c.sum())

#sum ~~> 0+0+0+1+1+1=3 bcz False=0 & True=1

#===========================

# Кількість елементів
print(heights_arr.size) 
#>> 45

# Форма (кількість елементів, кільксть рівнів)
print(heights_arr.shape)
#>> (45,)


#======== Example ==========
arr1 = np.array([1,2,3])
print(arr1)
#>> [1 2 3]
print(arr1.size)
#>> 3 (means 3 members inside array)
print(arr1.shape)
#>> (3,) - its a 1 dimentional array

arr2 = np.array([[1,2,3], [3,4,6]])
print(arr2.size)
#>> 6 (means 6 members inside array)
print(arr2.shape)
#>> (2, 3) - its a 2 dimentional array

arr3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr3.size)
#>> 8 (means 8 members inside array)
print(arr3.shape)
#>> (2, 2, 2) - its a 3 dimentional array
#dimentions of an array we can identify with the number of square brackets in front of the array

#========= Example =======

a = np.array((1,2,3,4,5,6))

print('Size of a (1d)' , a.size)
print('Shape of a (1d)',a.shape)

b = np.array(((1,2),(3,4),(5,6)))
##############
# b = [[1 2]  \
#         [3 4]    3
#         [5 6]] /
#          \  /
#           2
##############
print(b.shape) # (3,2)
print(b.size)  # 6


"""
Numpy arrays functions 
"""

import numpy as np
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List:", list)
arr = np.array(list)
print("Numpy array:", arr)
print("Array size:", arr.size)
print("Array shape:", arr.shape)
arr2 = arr.reshape((2, 5))
print("Reshaped array:", arr2)
flist = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Float list:", flist)
farr = np.array(flist)
print("Float array:", farr)
blist = [True, False, False, True, True]
print("Boolean list:", blist)
barr = np.array(blist)
print("Boolean array:", barr)


"""
Numpy arrays reshape
"""

import numpy as np

A = ["a","b","c"]
B = ["x","y","z"]

C = A + B

# convert a list into a numpy array
D = np.array(C)

print (D.size)
print (D.shape)

#D.reshape format is (row,column). Same as Matrices.
print (D.reshape(2,3))
print (D.reshape(3,2))

#if you leave one entry as -1, numpy will automatically guess it for you. As a result, the array size (number of elements of the array) is kept the same.
print (D.reshape(2,-1))
print (D.reshape(-1,2))


"""
Тип даних
  Ще одна особливість масиву numpy в тому, що він однорідний, щоб кожен елемент мав мати один і той самий тип даних.
  Наприклад, у heights_arr ми записали всі висоти в цілих числах;  таким чином, кожен елемент зберігається як ціле число в масиві.  Щоб перевірити тип даних, використовуйте numpy.ndarray.dtype.
 Якщо ми змішуємо число з плаваючою точкою, скажімо, перший елемент буде 189,0 замість 189:
 Потім після перетворення списку в масиві ми побачимо, що всі інші числа приводяться в floats:
 Numpy підтримує кілька типів даних, таких як int (ціле число), float (числова плаваюча точка) і bool (логічні значення, True і False).  Номер після типу даних, напр.  int64, представляє розмір в бітах типу данних.
"""

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print(heights_arr.dtype)

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_float_arr = np.array(heights_float)
# print(heights_float_arr)
print("\n")
print(heights_float_arr.dtype)


"""
Numpy array indexes
"""

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print(heights_arr[2])

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
print(heights_and_ages_arr[1,2])

# Індексація двомірного масива
#     1     2     3     4     5 ...
# 1 [0,0] [0,1] [0,2] [0,3]  ...
# 2 [1,0] [1,1] [1,2] [1,3]   ...
# 3 [2,0] [2,1] [2,2] [2,3]   ...
# ...

# array indexing is same as list indexing

import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1[0])
#>> 1

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[1][0])  # array[row][column]
#>> 4
print(arr2[1,0])   ## array[row, column]
#>> 4

#slicing
arr1 = np.array([1,2,3,4,5])
print(arr1[1:3])
#>> [2 3]

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[0,:])  # row index zero and all columns
#>>  [1, 2, 3]
print(arr2[0,0:2])  # row index zero and first 2 columns
#>> [1 2]
print(arr2[:,1])  # all rows and only column index 1
#>> [2 5]

"""
5th Row is:
0
1
2
3
4

And 2nd Column is:
0 1

So rows index downwards starting from 0
Columns index left to right starting from 0
Hence (4,1) for 5th row and 2nd Column
"""

"""
Slicing (lesson summary)

[<row> START : STOP : STEP,  <column> START : STOP : STEP]

NumPy example:
"""

import numpy as np 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = np.array(a)

print(a) # -> [1,2,3,4,5,6,7,8,9] 
print(arr) # ->[1 2 3 4 5 6 7 8 9]

# Slicing... 
print(arr[: :2]) # ->[1 3 5 7 9]
print(arr[2: :]) # ->[3 4 5 6 7 8 9]
print(arr[:2:]) # ->[1 2]
print(arr[2:2:]) # ->[ ]
print(arr[2:2:2]) # ->[ ] 
print(arr[:2:2]) # -> [1]

# array indexing is same as list indexing

arr1 = np.array([1,2,3,4,5])
print(arr1[0])
#>> 1

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[1][0])  # array[row][column]
#>> 4
print(arr2[1,0])   ## array[row, column]
#>> 4

#slicing
arr1 = np.array([1,2,3,4,5])
print(arr1[1:3])
#>> [2 3]

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[0,:])  # row index zero and all columns
#>>  [1, 2, 3]
print(arr2[0,0:2])  # row index zero and first 2 columns
#>> [1 2]
print(arr2[:,1])  # all rows and only column index 1
#>> [2 5]


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
