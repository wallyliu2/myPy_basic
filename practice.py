# Section 1: Intro
# print('Wally is learning')
# name = input('What is your name?')
# print('Hello, ' + name +'!')

# Section 2: Data Type
# Section 2.1 Fundamental Data Types: int, float, bool, str, list, tuple, set, dict, complex

print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))
print(type(0))
print(type(20 + 1.1))

print(2**2)  # Power
print(2 // 4)  # Round down
print(5 % 4)  # Module

print(bin(5))  # show binary number

print(int('0b101', 2))  # base 2 (binary)

# Math functions
print(round(3, 9))
print(abs(-20))

# Operator precedence
print(20 - 3 * 4)  #8

print((5 + 4) * 10 / 2)  #45.0

print(((5 + 4) * 10) / 2)  #45.0

print((5 + 4) * (10 / 2))  #45.0

print(5 + (4 * 10) / 2)  #25.0

print(5 + 4 * 10 // 2)  #25

# Variables
score = 100
print(score)

a, b, c = 1, 2, 3  # assign multiple values at once
print(a)
print(b)
print(c)

# Augmented assignment Operator
some_value = 5
some_value += 2  # equal to some_value = some_value + 2
print(some_value)

# Data Type: String
greeting = 'hi there, this is Wally'
print(greeting)
print(type(greeting))

long_greeting = '''
  Wow
  0.0
  Hi
'''
print(long_greeting)

first_name = 'Wally'
last_name = ' Weber'
print(first_name + last_name)

print(type(str(100)))

# Escape Sequence
weather = "\t It\'s \"kind of\" sunny. \n hope you have a good day!"
print(weather)

# Formating string

name = 'Wally'
age = 20

print(f'hi {name}. You are {age} years old.')

# String index
# [start:stop]
full_name = 'Wally Weber'
print(full_name[:5])
print(full_name[-1])
print(full_name[::-1])  # reverse string

print(full_name.upper())
print(full_name.capitalize())
print(full_name.find('be'))
print(full_name.replace('Weber', 'Wber'))

#username = input('What is your username?')
#password = input('What is your password?')
#len_password = len(password)
#hidden_password = '*' * len_password # print('*' * 10)

#print(f'{username}, your password {hidden_password} is {len_password} letters long')

# List
li = [1, 2]
li2 = ['a', 'b']
li3 = ['a', 3, True]
print(li3[2])
print(li3[:2])
li3[0] = 'b'
print(li3[:])

# Important Concept: Copy vs. Modify
amazon_cart = ['notebook', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
# new_cart = amazon_cart # Modify
new_cart = amazon_cart[:]  # Copy
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][2])

# Adding elements
basket = [1, 2, 3, 4, 5]
basket.append(100)
basket.insert(2, 100)
print(basket)

# Removing elements
basket.pop()
print(basket)
basket.pop(1)
print(basket)
basket.remove(100)
print(basket)
basket.clear()
print(basket)

# Finding the element's index
basket = [1, 2, 3, 4, 5, 1]
print(basket.index(2))
print(1 in basket)
print(100 in basket)
print(basket.count(2))  # count how many times the element showing in the list
print(sorted(basket))  # sort the list
basket.sort()
basket.reverse()
print(basket)
print(len(basket))
print(basket[::-1])  # reverse again

# Create a series of numbers
print(list(range(1, 100)))
print(list(range(101)))

# Join List
sentence = ' '.join(['hi', 'my', 'name', 'is', 'wally'])
print(sentence)

# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6]

print(a)
print(b)
print(c)
print(other)
print(d)

# None dataype
weapons = None
print(weapons)

# Dictionary, there is no order for dictionary, not like list data structure (with orders)
dictionary = {'a': 1, 'b': 2}  # key is a string

dictionary = {'a': [1, 2, 3], 'b': 'hello', 'c': True}

print(dictionary['b'])  # Look for a key called b

my_list = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True
}, {
    'a': [4, 5, 6],
    'b': 'hi',
    'c': False
}]

print(my_list[0]['a'][2])

dictionary = {
    123: [1, 2, 3],
    True: 'hello',
    'c': True
}  # key cannot change, but list cannot be used because it's changable, most keys are string datatype, key needs to be unique

user = {'basket': [1, 2, 3], 'greet': 'hello'}

print(
    user.get('age')
)  # check if the key exists, if not, the program would keep executing the rest

print(user.get('age'), 55)  # if the key doesn't exist, show the second value

# there is another way to create dictionary, but it's not common
user2 = dict(name='WallyWber')

print(user2)

print('basket' in user)
print('hello' in user.values())
print('basket' in user.keys())
print(user.items())  # this is tuple
user2 = user.copy()
print(user.clear())
print(user2)

# Tuples: like list but immutable, faster than list

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)
print(user.items())  # this is tuple

new_tuple = my_tuple[1:4]
print(new_tuple)
x, y, z, *other = (1, 2, 3, 4, 5)

print(my_tuple.count(2))
print(my_tuple.index(4))
print(len(my_tuple))

# Sets: is a unorder unique collection  (no duplicate)
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(5)
my_set.add(100)
print(my_set)  # only show uniqe values

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # turn list into set

my_set = {1, 2, 3, 4, 5, 5}
print(1 in my_set)
print(len(my_set))
# my_set.copy()
# my_set.clear()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8}

# difference
print(my_set.difference(your_set))

# discard
print(my_set.discard(5))
print(my_set)

# difference_update
print(my_set.difference_update(your_set))
print(my_set)

# intersection
print(my_set.intersection(your_set))
print(my_set & your_set)  # same as above

# isdisjoint
print(my_set.isdisjoint(your_set))

# union
print(my_set.union(your_set))
print(my_set | your_set)  # same as above

# issubset
print(my_set.issubset(your_set))

# issuperset
print(my_set.issuperset(your_set))

# Constants, PI = 3.14
# Sys __

# Section 2.2 Classes -> Custom Type

# Section 2.3 Specialized Data Types

# Conditional Logic
is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive")
elif is_licensed:
    print("You can drive now!")
else:
    print("Not yet")

# Truthy and Falsy

# Ternary Operator
# condition_if_true if condition else condition_if_false
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# Short Circuiting
is_Friend = False
is_User = True

if is_Friend or is_User:
  print("best friends forever")

if is_Friend and is_User:
  print("best friends forever")

# Logical Operator: >, <. ==, or, and
print(4==5) # cannot use = because the = is assigning

is_magician = True
is_expert = False

# check if magician AND expert: "you are a master magician"
# check if magician but not expert: "at least you're getting there"
# check if you're not a magician: "you need magic powers"

if is_magician and is_expert:
  print("you are a master magician")
elif not is_expert and is_magician:
  print("you are getting there")
else:
  print("you need magic power.")

# is (store in location) vs. ==
print(True == 1) # True
print(' ' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True
print('1' == 1) # False

print(True is 1) # False
print(' ' is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([1,2,3] is [1,2,3]) # False
print('1' is '1') # True

# Loop - FOR
for item in 'Zero to Mastery':
  print(item)

for item in (1,2,3,4,5):
  for x in ['a',
  'b','c']:
    print(item, x)

# Iterable - list, dictionary, tuple, set, string
# Iterate -> one by one check each item in the collection

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for item in user:
  print(item)

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for key, value in user.items():
  print(key, value)

# Build a counter via for loop
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for n in my_list:
  #print(n)
  counter = counter + n
print(counter)

# range()
print(range(100)) # range object

for number in range(0,10):
  print(number)

for number in range(0,4):
  print('print')

for _ in range (0,10,2):
  print(_)

for _ in range(10,0,-1):
  print(_)

for _ in range(2):
  print(list(range(10)))

# enumerate()
for i,char in enumerate('Hellooo'):
  print(i,char)

for i,char in enumerate((1,2,3)):
  print(i,char)

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f'index of 50 is {i}')

# while
i = 0
while i < 50:
  print(i)
  i += 1
  # break
else:
  print('done with all the work')

my_list = [1,2,3]

for item in my_list:
  print(item)

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1

#while True:
  #response = input('say something:')
  #if (response == 'bye'):
    #break

for item in my_list:
  continue
  print(item) # It would not be executed

# Our first GUI
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel == 0:
          print(empty, end ='')
        elif pixel == 1:
          print(fill, end = '')
    print('')

some_list = ['a','b','c','b','d','m','n','n']
some_list_unique = list(set(some_list))
print(some_list_unique)

duplicate = set([x for x in some_list if some_list.count(x) > 1])

print(list(duplicate))

# the other way to find duplicate
duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

# Function
def say_hello():
  print("hello")

say_hello()

# Avoid repetition
def show_tree():
  picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
  ]
  fill = '*'
  empty = ' '
  for row in picture:
    for pixel in row:
        if pixel == 0:
          print(empty, end ='')
        elif pixel == 1:
          print(fill, end = '')
    print('')

show_tree()
show_tree()

# Parameters
def say_hello(name, emoji):
  print(f'hello, {name} {emoji}.')

# positional arguments
say_hello('Wally',':)') # call, invoke

# keyword arguments
say_hello(name='Weber', emoji=':P')

# Default parameters
def say_hello(name='default', emoji='^^'):
  print(f'hello, {name} {emoji}.')

say_hello()

# Function - return
# Function should do one thing really well and return something
def sum(num1, num2):
  print(f'{num1} + {num2} = ', end='')
  return num1+num2
  
total = sum(3,4)
print(total)

def sum(num1, num2):
  def another_func(n1,n2):
    return n1+n2
  return another_func(num1,num2)
  print('hello') # won't execute because return would exit the function right away

# Exercise

age = input("What is your age?: ")

if int(age) < 18:
  print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
  print("Powering On. Enjoy the ride!");
elif int(age) == 18:
  print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def checkDriverAge():
  age = input("What is your age?: ")

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(92)
checkDriverAge()

# Docstrings
def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)

test('1111')
help(test)
print(test.__doc__)

# *args: accept any values

def super_func(*args):
  print(args)
  return sum(args)

print(super_func(1,2,3,4))

# **kwargs: accept keywords
def super_func1(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args)+ total

print(super_func1(1,2,3,4, num1=5, num2=4))

# Rule: params, *args, default parameters, **kwargs

# Exercise - Create a fuction that can be used to find the max even number in a list
# Solution 1 (My version)
def highest_even(li):
  li = sorted(li)
  li = li[::-1]
  for items in li:
    if items % 2 == 0:
      return items
      break

list_1 = [1,2,3,4,5,6,7,8,9,10,11]

list_2 = [3,6,1,6,8,100,201]

print(highest_even(list_1))
print(highest_even(list_2))

# Solution 2 (Andrei's version)
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

list_1 = [1,2,3,4,5,6,7,8,9,10,11]

list_2 = [3,6,1,6,8,100,201]

print(highest_even(list_1))
print(highest_even(list_2))

# Scope: what variables do I have access to
# priority: local > parent local > global > built in python functions

a = 1 # global scope
def confusion():
  a = 5 # function scope
  return a

print(a) # print global variable
print(confusion()) # print function variable
# global keyword, nonlocal keyword

# map()
# map(action, obj)
my_list = [1,2,3]
def multiply_by2(item):
  return item*2

print(list(map(multiply_by2, my_list))) # map already created function memory, so when using function, we don't need to put ()

print(my_list)

# filter()

def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, my_list)))

# zip()
my_list = [1,2,3]
your_list = (10,20,30)

print(list(zip(my_list, your_list))) # create a tuple

# reduce()
from functools import reduce
# reduce(acc, item)
my_list = [1,2,3]

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(reduce(accumulator, my_list, 0))

print(reduce(accumulator, my_list, 10))

# list comprehensions
my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(0,100)]

my_list3 = [num*2 for num in range(1,100)]

my_list4 = [num*2 for num in range(1,100) if num%2 ==0]

print(my_list4)

# set comprehensions
my_list = {char for char in 'hello'}
print(my_list)

# dictionary comprehensions
simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = {
  key: value**2 for key, value in simple_dict.items() if value % 2 ==0
}

print(my_dict)

my_dict1 = {
  num: num*2 for num in {1,2,3}
}

print(my_dict1)

# Using compresion to solve the duplicate issue

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([val for val in some_list if some_list.count(val)>1]))

print(duplicates)