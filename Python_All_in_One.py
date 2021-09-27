# age = input("How old are you")
# age = int(age)
# print(age)

# Strings
type('Hellloooooo') # str

'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab

'Hey you!'[4] # y
name = 'Shivam Chhetry'
# print(name[4])     # a
# print(name[:])     # Shivam Chhetry
# print(name[1:])    # hivam chhetry
# print(name[:1])    # A
# print(name[-1])    # y
# print(name[::1])   # Shivam Chhetry
# print(name[::-1])  # yrtehhC mavihS
# print(name[0:10:2])  # Sia h
# # : is called slicing and has the format [ start : end : step ]
#
# print('Hi there ' + 'Timmy')  # 'Hi there Timmy' --> This is called string concatenation
# print('*'*10)  # **********

""" Basic Functions """
# print(len('Data Science'))  # 12
#
# # Basic Methods
# print('  I am alone '.strip())               # 'I am alone' --> Strips all whitespace characters from both ends.
# print('On an island'.strip('d'))             # 'On an islan' --> # Strips all passed characters from both ends.
# print('but life is good!'.split())           # ['but', 'life', 'is', 'good!']
# print('Help me'.replace('me', 'you'))        # 'Help you' --> Replaces first with second param
# print('Need to make fire'.startswith('Need')) # True
# print('and cook rice'.endswith('rice'))      # True
# print('bye bye'.index('e'))                  # 2
# print('still there?'.upper())                # STILL THERE?
# print('HELLO?!'.lower())                     # hello?!
# print('ok, I am done.'.capitalize())         # 'Ok, I am done.'
# print('oh hi there'.find('i'))               # 4 --> returns the starting index position of the first occurrence
# print('oh hi there'.count('e'))              # 2



# String Formatting
# name1 = 'Andrei'
# name2 = 'Sunny'
# print(f'Hello there {name1} and {name2}')       # Hello there Andrei and Sunny - Newer way to do things as of python 3.6
# print('Hello there {}, {}'.format(name1, name2))# Hello there Andrei and Sunny
# print('Hello there %s and %s' %(name1, name2))  # Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string representations of objects respectively


# Palindrome check
word = 'mom'
# p = bool(word.find(word[::-1]) + 1)
# print(p)  # True

""" Lists """
my_list = [1, 2, '3', True] # We assume this list won't mutate for each example below
# print(len(my_list))             # 4
# print(my_list.index('3'))         # 2
# print(my_list.count(2))           # 1 --> count how many times 2 appears
#
# print(my_list[3])                 # True
# print(my_list[1:])                # [2, '3', True]
# print(my_list[:1])                # [1]
# print(my_list[-1])               # True
# print(my_list[::1])               # [1, 2, '3', True]
# print(my_list[::-1])              # [True, '3', 2, 1]
# print(my_list[0:3:2])             # [1, '3']

# : is called slicing and has the format [ start : end : step ]

# Add to List
# print(my_list * 2)                # [1, 2, '3', True, 1, 2, '3', True]
# print(my_list + [100])            # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
# print(my_list.append(100))        # None --> Mutates original list to [1, 2, '3', True, 100]          # Or: <list> += [<el>]
# print(my_list.extend([100, 200])) # None --> Mutates original list to [1, 2, '3', True, 100, 200]
# print(my_list.insert(2, '!!!'))   # None -->  [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.
#
# print(' '.join(['Hello','There'])) # 'Hello There' --> Joins elements using string as separator.

# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]
# print(new_basket)
# print(new_basket2)

# Remove from List
[1,2,3].pop()    # 3 --> mutates original list, default index in the pop method is -1 (the last item)
[1,2,3].pop(1)   # 2 --> mutates original list
[1,2,3].remove(2)# None --> [1,3] Removes first occurrence of item or raises ValueError.
[1,2,3].clear()  # None --> mutates original list and removes all items: []
del [1,2,3][0] #

# Ordering
[1,2,5,3].sort()         # None --> Mutates list to [1, 2, 3, 5]
[1,2,5,3].sort(reverse=True) # None --> Mutates list to [5, 3, 2, 1]
[1,2,5,3].reverse()      # None --> Mutates list to [3, 5, 2, 1]
sorted([1,2,5,3])        # [1, 2, 3, 5] --> new list created
list(reversed([1,2,5,3]))# [3, 5, 2, 1] --> reversed() returns an iterator

# Useful operations
1 in [1,2,5,3]  # True
min([1,2,3,4,5])# 1
max([1,2,3,4,5])# 5
sum([1,2,3,4,5])# 15


# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(matrix[2][0])

# Looping through a matrix by rows:
# mx = [[1, 2, 3], [4, 5, 6]]
# for row in range(len(mx)):
#     for col in range(len(mx[0])):
#         print(mx[row][col])  # 1 2 3 4 5 6
#
# # Transform into a list:
# print([mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))])  # [1,2,3,4,5,6]
#
# # Combine columns with zip and *:
# print([x for x in zip(*mx)])  # [(1, 4), (2, 5), (3, 6)]
#

# List Comprehensions
# new_list[<action> for <item> in <iterator> if <some condition>]
a = [i for i in 'hello']                  # ['h', 'e', 'l', 'l', '0']
b = [i*2 for i in [1,2,3]]                # [2, 4, 6]
c = [i for i in range(0,10) if i % 2 == 0]# [0, 2, 4, 6, 8]

""" Dictionaries """
my_dict = {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False}
# print(my_dict['name'])                      # Andrei Neagoie
# print(len(my_dict))                         # 3
# print(list(my_dict.keys()))                 # ['name', 'age', 'magic_power']
# print(list(my_dict.values()))               # ['Andrei Neagoie', 30, False]
# print(list(my_dict.items()))                # [('name', 'Andrei Neagoie'), ('age', 30), ('magic_power', False)]
# my_dict['favourite_snack'] = 'Grapes' # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes'}
# print(my_dict.get('age'))                   # 30 --> Returns None if key does not exist.
# print(my_dict.get('ages', 0 ))              # 0 --> Returns default (2nd param) if key is not found

#Remove key
del my_dict['name']
print(my_dict.pop('name', None))

my_dict.update({'cool': True})                                         # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
print({**my_dict, **{'cool': True} })                                         # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
new_dict = dict([['name','Shivam'],['age',32],['magic_power',False]])  # Creates a dict from collection of key-value pairs.
new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False]))# Creates a dict from two collections.
print(new_dict)



""" Tuples """
my_tuple = ('apple','grapes','mango', 'grapes')
apple, grapes, mango, grapes = my_tuple# Tuple unpacking
len(my_tuple)                          # 4
my_tuple[2]                            # mango
my_tuple[-1]                           # 'grapes'

# Immutability
# my_tuple[1] = 'donuts'  # TypeError
# my_tuple.append('candy')# AttributeError

# Methods
my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2

# Zip
list(zip([1,2,3], [4,5,6])) # [(1, 4), (2, 5), (3, 6)]

# unzip
z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
unzip = lambda z: list(zip(*z))
unzip(z)


""" Sets """
my_set = set()
my_set.add(1)  # {1}
my_set.add(100)# {1, 100}
my_set.add(100)# {1, 100} --> no duplicates!

new_list = [1,2,3,3,3,4,4,5,6,1]
set(new_list)           # {1, 2, 3, 4, 5, 6}

my_set.remove(100)      # {1} --> Raises KeyError if element not found
my_set.discard(100)     # {1} --> Doesn't raise an error if element not found
my_set.clear()          # {}
new_set = {1,2,3}.copy()# {1,2,3}

set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)               # {1,2,3,4,5}
set4 = set1.intersection(set2)        # {3}
set5 = set1.difference(set2)          # {1, 2}
set6 = set1.symmetric_difference(set2)# {1, 2, 4, 5}
set1.issubset(set2)                   # False
set1.issuperset(set2)                 # False
set1.isdisjoint(set2)                 # False --> return True if two sets have a null intersection.


""" Logical Operators """
# 1 < 2 and 4 > 1 # True
# 1 > 3 or 4 > 1  # True
# 1 is not 4      # True
# not True        # False
# 1 not in [2,3,4]# True

# if <condition that evaluates to boolean>:
#   # perform action1
# elif <condition that evaluates to boolean>:
#   # perform action2
# else:
#   # perform action3


""" Loops """
# my_list = [1,2,3]
# my_tuple = (1,2,3)
# my_list2 = [(1,2), (3,4), (5,6)]
# my_dict = {'a': 1, 'b': 2,'c': 3}
#
# for num in my_list:
#     print(num) # 1, 2, 3
#
# for num in my_tuple:
#     print(num) # 1, 2, 3
#
# for num in my_list2:
#     print(num) # (1,2), (3,4), (5,6)
#
# for num in '123':
#     print(num) # 1, 2, 3
#
# for k,v in my_dict.items(): # Dictionary Unpacking
#     print(k) # 'a', 'b', 'c'
#     print(v) # 1, 2, 3

# while <condition that evaluates to boolean>:
#   # action
#   if <condition that evaluates to boolean>:
#     break # break out of while loop
#   if <condition that evaluates to boolean>:
#     continue # continue to the next line in the block


""" Range """
range(10)          # range(0, 10) --> 0 to 9
range(1,10)        # range(1, 10)
list(range(0,10,2))# [0, 2, 4, 6, 8]

""" Enumerate """
# for i, el in enumerate('helloo'):
#   print(f'{i}, {el}')
# 0, h
# 1, e
# 2, l
# 3, l
# 4, o
# 5, o


""" Counter """
from collections import Counter
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)# Counter({'blue': 3, 'red': 2, 'yellow': 1})
counter.most_common()[0] # ('blue', 3)


""" Functions 
*args and **kwargs
Splat (*) expands a collection into positional arguments,
while splatty-splat (**) expands a dictionary into keyword arguments.
"""
args   = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
# some_func(*args, **kwargs) # same as some_func(1, 2, x=3, y=4, z=5)
"""
Splat combines zero or more positional
arguments into a tuple, while splatty-splat
combines zero or more keyword arguments into a dictionary.
"""
def add(*a):
    return sum(a)

print(add(1, 2, 3)) # 6

def f(*args):                  # f(1, 2, 3)
def f(x, *args):               # f(1, 2, 3)
def f(*args, z):               # f(1, 2, z=3)
def f(x, *args, z):            # f(1, 2, z=3)

def f(**kwargs):               # f(x=1, y=2, z=3)
def f(x, **kwargs):            # f(x=1, y=2, z=3) | f(1, y=2, z=3)

def f(*args, **kwargs):        # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*args, y, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, *args, z, **kwargs):  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)

# Other Uses of *
[*[1, 2, 3], *[4]]  # [1, 2, 3, 4]
{*[1, 2, 3], *[4]}  # {1, 2, 3, 4}
(*[1, 2, 3], *[4])  # (1, 2, 3, 4)
{**{'a': 1, 'b': 2}, **{'c': 3}}  # {'a': 1, 'b': 2, 'c': 3}

head, *body, tail = [1,2,3,4,5]
head # 1
tail # 5


""" Lambda """
# lambda: <return_value>
# lambda <argument1>, <argument2>: <return_value>
# Factorial
from functools import reduce

n = 3
factorial = reduce(lambda x, y: x*y, range(1, n+1))
print(factorial) #6

# Fibonacci
fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
result = fib(10)
print(result) #55

""" Comprehensions """
<list> = [i+1 for i in range(10)]         # [1, 2, ..., 10]
<set>  = {i for i in range(10) if i > 5}  # {6, 7, 8, 9}
<iter> = (i+5 for i in range(10))         # (5, 6, ..., 14)
<dict> = {i: i*2 for i in range(10)}      # {0: 0, 1: 2, ..., 9: 18}

output = [i+j for i in range(3) for j in range(3)] # [0, 1, 2, 1, 2, 3, 2, 3, 4]

# Is the same as:
output = []
for i in range(3):
  for j in range(3):
    output.append(i+j)


""" Ternary Condition """
# <expression_if_true> if <condition> else <expression_if_false>

[a if a else 'zero' for a in [0, 1, 0, 3]] # ['zero', 1, 'zero', 3]

""" Map Filter Reduce """
from functools import reduce
list(map(lambda x: x + 1, range(10)))            # [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list(filter(lambda x: x > 5, range(10)))         # (6, 7, 8, 9)
reduce(lambda acc, x: acc + x, range(10))        # 45

""" Any All """
any([False, True, False])# True if at least one item in collection is truthy, False if empty.
all([True,1,3,True])     # True if all items in collection are true

""" Closures 
We have a closure in Python when:
1. A nested function references a value of its enclosing function and then
2. the enclosing function returns the nested function.
"""
def get_multiplier(a):
    def out(b):
        return a * b
    return out
multiply_by_3 = get_multiplier(3)
multiply_by_3(10)   # 30


""" Modules """
if __name__ == '__main__': # Runs main() if file wasn't imported.
    main()

import <module_name>
from <module_name> import <function_name>
import <module_name> as m
from <module_name> import <function_name> as m_function
from <module_name> import *

""" Iterators 
In this cheatsheet '<collection>' can also mean an iterator.
"""
<iter> = iter(<collection>)
<iter> = iter(<function>, to_exclusive)     # Sequence of return values until 'to_exclusive'.
<el>   = next(<iter> [, default])           # Raises StopIteration or returns 'default' on end.

class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

n_list = Series(1,10)
print(list(n_list))

# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'shivam'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break
Output:
s
h
i
v
a
m

""" Decorators
A decorator takes a function, 
adds some functionality and returns it. 
"""
@decorator_name
def function_that_gets_passed_to_decorator():
    ...

""" Class """
class <name>:
    age = 80 # Class Object Attribute
    def __init__(self, a):
        self.a = a # Object Attribute

    @classmethod
    def get_class_name(cls):
        return cls.__name__

""" Inheritance """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num


""" Multiple Inheritance """
class A: pass
class B: pass
class C(A, B): pass


""" Exceptions """
try:
  5/0
except ZeroDivisionError:
  print("No division by zero!")
while True:
  try:
      x = int(input('Enter your age: '))
  except ValueError:
      print('Oops!  That was no valid number.  Try again...')
  else:  # code that depends on the try block running successfully should be placed in the else block.
      print('Carry on!')
      break

""" Raising Exceptions """
raise ValueError('some error message')

""" Finally """
try:
    raise KeyboardInterrupt
except:
    print('oops')
finally:
    print('All done')

""" File IO
<file> = open('<path>', mode='r', encoding=None)

Modes
'r' - Read (default).
'w' - Write (truncate).
'x' - Write or fail if the file already exists.
'a' - Append.
'w+' - Read and write (truncate).
'r+' - Read and write from the start.
'a+' - Read and write from the end.
't' - Text mode (default).
'b' - Binary mode.
"""

""" File """
<file>.seek(0)                      # Moves to the start of the file.
<str/bytes> = <file>.readline()     # Returns a line.
<list>      = <file>.readlines()    # Returns a list of lines.
<file>.write(<str/bytes>)           # Writes a string or bytes object.
<file>.writelines(<list>)           # Writes a list of strings or bytes objects.

""" Read Text From File """
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines() # or read()

for line in read_file(filename):
  print(line)

""" Write Text to File """
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

""" Append Text to File """
def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)


""" Useful Libraries """
"""CSV"""
import csv

# Read Rows from CSV File
def read_csv_file(filename):
    with open(filename, encoding='utf-8') as file:
        return csv.reader(file, delimiter=';')

# Write Ros to CSV file
def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)

""" JSON """
import json
<str>    = json.dumps(<object>, ensure_ascii=True, indent=None)
<object> = json.loads(<str>)

# Read Object from JSON file
def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)

# Write Oject to JSON file
def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)

""" Pickle """
import pickle
<bytes>  = pickle.dumps(<object>)
<object> = pickle.loads(<bytes>)

# Read Object from file
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Write Oject to File
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)

""" Profile """
# Basic
from time import time
start_time = time()  # Seconds since
...
duration = time() - start_time

# math
from math import e, pi
from math import cos, acos, sin, asin, tan, atan, degrees, radians
from math import log, log10, log2
from math import inf, nan, isinf, isnan

# Statistics
from statistics import mean, median, variance, pvariance, pstdev

# Random
from random import random, randint, choice, shuffle
random() # random float between 0 and 1
randint(0, 100) # random integer between 0 and 100
random_el = choice([1,2,3,4]) # select a random element from list
shuffle([1,2,3,4]) # shuffles a list

""" Datetime 
1. Module 'datetime' provides 'date' <D>, 'time' <T>, 'datetime' <DT> and 'timedelta' <TD> classes. All are immutable and hashable.
2. Time and datetime can be 'aware' <a>, meaning they have defined timezone, or 'naive' <n>, meaning they don't.
3. If object is naive it is presumed to be in system's timezone.
"""
from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz

"""Regex"""
import re
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences.
<list>  = re.findall(<regex>, text)            # Returns all occurrences.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to keep the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.



