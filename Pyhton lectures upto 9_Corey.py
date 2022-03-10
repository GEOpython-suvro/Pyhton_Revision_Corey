"""Video lecture 2: String"""
greetings = "Hello"
name = "Michael"
print(greetings+", "+ name) #TERMINAL:Hello, Michael
print(len(greetings+", "+ name)) #TERMINAL:14
print(name[2]) #TERMINAL:c
print(name[-1]) #TERMINAL:l
print(name[:4]) #TERMINAL:Mich
print(name[1:3])  #TERMINAL:ic
my_message="{},{}".format(greetings.upper(), name)
print(my_message) #TERMINAL:HELLO,Michael

message= "Hello world"
print(message[6:]) #TERMINAL:world
print(message.count("l")) #TERMINAL:3
print(message.find("world")) #TERMINAL:6
print(message.find("universe")) #TERMINAL:-1
new_message=message.replace("world","universe")
print(new_message) #TERMINAL:Hello universe

"""Video lecture 3:  Integers and Floats - Working with Numeric Data 
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2"""
print(2%2) #TERMINAL:0
print(3%2) #TERMINAL:1
print(4%2) #TERMINAL:0
print(5%2) #TERMINAL:1
print(3*2+1) #TERMINAL:7
num=1
num +=10
print(num) #TERMINAL:11

numb=2
numb*=22
print(numb) #TERMINAL:44

print(abs(-3)) #TERMINAL:3
print(round(3.75,1)) #TERMINAL:3.8

num_1 = 3
num_2 =2
print(num_1==num_2) #TERMINAL:False
print(num_1!=num_2) #TERMINAL:True
print(num_1>=num_2) #TERMINAL:True
print(num_1<=num_2) #TERMINAL:False

numb_1="100"
numb_2="200"
numb_1=int(numb_1)
numb_2=int(numb_2)
print(numb_1+numb_2) #TERMINAL:300

"""Video lecture 4: Lists, Tuples, and Sets"""
list_of_courses= ['History','Math','Physics','Compsci']
nums=[1,2,3,4,5]
print(list_of_courses[-1]) #TERMINAL:Compsci
print(list_of_courses[:2]) #TERMINAL:['History', 'Math']
print(list_of_courses[2:]) #TERMINAL:['Physics', 'Compsci']
list_of_courses.insert(0, 'Art')
print(list_of_courses) #TERMINAL:['Art', 'History', 'Math', 'Physics', 'Compsci']

courses_2= ['Art','Education']
list_of_courses.extend(courses_2)
print(list_of_courses) #TERMINAL: ['History', 'Math', 'Physics', 'Compsci', 'Art', 'Education']

list_of_courses.remove('Math')
print(list_of_courses) #TERMINAL: ['History', 'Physics', 'Compsci']

popped=list_of_courses.pop()
print(popped) #TERMINAL: Compsci
print(list_of_courses) #TERMINAL:['History', 'Math', 'Physics']

list_of_courses.reverse()
print(list_of_courses) #TERMINAL:['Compsci', 'Physics', 'Math', 'History']

list_of_courses.sort()
nums.sort()
print(list_of_courses) #TERMINAL:['Compsci', 'History', 'Math', 'Physics']
print(nums) #TERMINAL:[1, 2, 3, 4, 5]

list_of_courses.sort(reverse=True)
nums.sort(reverse=True)
print(list_of_courses) #TERMINAL:['Physics', 'Math', 'History', 'Compsci']
print(nums) #TERMINAL:[5, 4, 3, 2, 1]

sorted_courses=sorted(list_of_courses)
print(sorted_courses) #TERMINAL:['Compsci', 'History', 'Math', 'Physics']

print(min(nums)) #TERMINAL:1
print(max(nums)) #TERMINAL:5
print(sum(nums)) #TERMINAL:15

print(list_of_courses.index('Math')) #TERMINAL:1
print('Math' in list_of_courses) #TERMINAL:True

for item in list_of_courses:
    print(item) #TERMINAL:History Math Physics Compsci

for index, item in enumerate(list_of_courses):
    print(index, item) #TERMINAL: 0 History  1 Math  2 Physics  3 Compsci

for index, item in enumerate(list_of_courses,start=1):
    print(index, item) #TERMINAL:1 History 2 Math 3 Physics 4 Compsci

list_of_courses_str= ', '.join(list_of_courses)
print(list_of_courses_str) #TERMINAL:History, Math, Physics, Compsci

list_of_courses_str= '- '.join(list_of_courses)
# print(list_of_courses_str) #TERMINAL:History- Math- Physics- Compsci
new_list_of_courses=list_of_courses_str.split('-')
print(new_list_of_courses) #TERMINAL:['History', ' Math', ' Physics', ' Compsci']

"""Tuples can't be modified unlike List"""
"""Mutable"""
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
# print(list_1) #TERMINAL: ['History', 'Math', 'Physics', 'CompSci']
# print(list_2) #TERMINAL: ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1) #TERMINAL: ['Art', 'Math', 'Physics', 'CompSci']
print(list_2) #TERMINAL: ['Art', 'Math', 'Physics', 'CompSci']

"""Immutable"""
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1) #TERMINAL:('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) #TERMINAL:('History', 'Math', 'Physics', 'CompSci')

"""Tuple can't be changed,following is error"""
tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2) #TERMINAL:TypeError: 'tuple' object does not support item assignment

"""Sets are unordered list if we run the Sets"""
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'biology'}
print(cs_courses) #TERMINAL:{'Math', 'History', 'Physics', 'CompSci'}
print('Math' in cs_courses) #TERMINAL:True

"""Empty Lists"""
empty_list = []
empty_list = list()

"""Empty Tuples"""
empty_tuple = ()
empty_tuple = tuple()

"""Empty Sets"""
empty_set = {} # This isn't right! It's a dict
empty_set = set()
print(cs_courses.intersection(art_courses)) #TERMINAL:{'History', 'Math'}
print(cs_courses.difference(art_courses)) #TERMINAL:{'Physics', 'CompSci'}
print(cs_courses.union(art_courses)) #TERMINAL:{'Math', 'biology', 'History', 'Art', 'Physics', 'CompSci'}

"""Video lecture 5: Dictionaries - Working with Key-Value Pairs"""
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name':'Suvro','age': 27,'phone':'555-555-5555'})

"""To delete any key-value pairs"""
del student['age']
print(student) #TERMINAL:{'name': 'Suvro', 'courses': ['Math', 'CompSci'], 'phone': '555-555-5555'}

print(len(student)) #TERMINAL:4
print(student.keys()) #TERMINAL:dict_keys(['name', 'age', 'courses', 'phone'])
print(student.items()) #TERMINAL:dict_items([('name', 'Suvro'), ('age', 27), ('courses', ['Math', 'CompSci']), ('phone', '555-555-5555')])

for keys in student.keys():
    print(keys) #TERMINAL: name age courses phone

for key, value in student.items():
    print(key, value) #TERMINAL: name Suvro    age 27     courses ['Math', 'CompSci']    phone 555-555-5555

"""Video 6: Conditionals and Booleans - If, Else, and Elif Statements
Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is """

if True:
    print('Conditional was True') 
if False:
    print('Conditional was True') #TERMINAL:Conditional was True

language='pyhton'
if language == 'pyhton':
    print('Language is Python')
else:
    print('No Match') #TERMINAL:Language is Python

language='Java'
if language == 'pyhton':
    print('Language is Python')
else:
    print('No Match')  #TERMINAL:No Match

language='Java'
if language == 'pyhton':
    print('Language is Python')
elif language == 'Java': 
    print('Language is Java')  
elif language == 'Javascript': 
    print('Language is Javascript') 
else:
    print('No Match') #TERMINAL:Language is Java

"""Comparisons
# and 
# or 
# not"""
user ='Admin'
logged_in = True
if user == 'Admin' and logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials') #TERMINAL:Admin Page

user ='Admin'
logged_in = False
if user == 'Admin' and logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials') #TERMINALBad Credentials

user ='Admin'
logged_in = False
if user == 'Admin' or logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials') #TERMINAL:Admin Page

user ='Admin'
logged_in = False   
if not logged_in:
    print('Please log in')
else:
    print('Welcome!') #TERMINAL:Please log in

a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7]
print(a==b) #TERMINAL:True
print(a is b) #TERMINAL:False

b=a
print(id(a)) #TERMINAL:2214880052416
print(id(b)) #TERMINAL:2214880052416
print(a is b) #TERMINAL: True

""" False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '', (), [].
#     Any empty mapping. For example, {}."""

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False


condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False


condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False


condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to False

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') #TERMINAL:Evaluated to True

"""Video lecture 7: Loops and Iterations - For/While Loops"""
numeric = [1,2,3,4,5,6,7]
for no in numeric:
    print(no) #TERMINAL: 1 2 3 4 5 6 7

"""let's find out the number 3 from numeric"""
numeric = [1,2,3,4,5,6,7]
for no in numeric:
    if no==3:
        print('Found!')
        break
    print(no) #TERMINAL: 1   2   Found!

numeric = [1,2,3,4,5,6,7]
for no in numeric:
    if no==3:
        print('Found!')
        continue
    print(no) #TERMINAL: 1   2   Found! 4 5 6 7

numeric = [1,2,3,4,5,6,7]
for no in numeric:
    for letter in 'abc':
        print(no,letter) #TERMINAL: 1 a 1 b  1 c 2 a 2 b 2 c 3 a 3 b 3 c 4 a 4 b 4 c 5 a 5 b 5 c 6 a 6 b 6 c 7 a 7 b 7 c

for i in range(10):
    print(i) #TERMINAL: 0 1 2 3 4 5 6 7 8 9

for i in range(1,11):
    print(i) #TERMINAL: 1 2 3 4 5 6 7 8 9 10 11

x=0
while x<10:
    print(x)
    x+=1  #TERMINAL: 0 1 2 3 4 5 6 7 8 9

x=0
while x<10:
    if x==5:
        break
    print(x)
    x+=1  #TERMINAL: 0 1 2 3 4

x=0
while True:
    if x==5:
        break
    print(x)
    x+=1 #TERMINAL: 0 1 2 3 4

"""to stop the following press ( Ctrl+C)"""
x=0
while True:
    print(x)
    x+=1

"""Video lecture 8: Functions
#following doesn't have a return value,so will print None"""
def hello_func():
    pass
print(hello_func()) #TERMINAL:None 

"""to run the above """
def hello_func():
    print("Hello Function!")
hello_func() #TERMINAL:Hello Function!

def hello_func():
    print("Hello Function!")
hello_func()
hello_func()
hello_func()
hello_func() #TERMINAL:Hello Function! Hello Function! Hello Function! Hello Function! 

"""If your boss orders to remove '!' sign,just change inside the print statement onetime and it will change all ! sign 
#This is calle keeping your cod 'DRY' meaning don't repeat urself"""
def hello_func():
    print("Hello Function.")
hello_func()
hello_func()
hello_func()
hello_func() #TERMINAL:Hello Function.Hello Function.Hello Function.Hello Function.

"""What does return mean and do in function?"""
def hello_func():
    return "Hello Function."
hello_func() #TERMINAL: nothing will show in terminal

def hello_func():
    return "Hello Function."
print(hello_func()) #TERMINAL: Hello Function. This is how function works. Just focus on input and return value and then print.

def hello_func():
    return "Hello Function."
print(hello_func().upper()) #TERMINAL:HELLO FUNCTION.

"""Input some parameters"""
def hello_func(greetings):
    return "{} Function.".format(greetings)
print(hello_func("Hi")) #TERMINAL: Hi Function.

def hello_func(greetings,name='You'):
    return "{}, {}.".format(greetings,name)
print(hello_func("Hi")) #TERMINAL:Hi, You.

def hello_func(greetings,name='You'):
    return "{}, {}.".format(greetings,name)
print(hello_func("Hi",name='Corey')) #TERMINAL:Hi, Corey.

def student_info(*args, **kwargs):
    print(args) #Tuples
    print(kwargs) #Dictionary
student_info('Math','Physics',name='John',age=24) #TERMINAL:('Math', 'Physics')
                                                           #{'name': 'John', 'age': 24}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses=['Math','Physics']
info={'name':'John','age':24}
student_info(*courses, **info) #TERMINAL:('Math', 'Physics')
                                        #{'name': 'John', 'age': 24}

""" Number of days per month. First value placeholder for indexing purposes."""
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017)) #TERMINAL:False
print(is_leap(2020)) #TERMINAL: True
print(days_in_month(2017, 2)) #TERMINAL:28

"""Video lecture 9: Import Modules and Exploring The Standard Library('my_module.py' is a file name in the dirkty)"""
import my_module
courses = ['History', 'Math', 'Physics', 'CompSci']
index=my_module.find_index(courses,'Math')
print(index) #TERMINAL:1

import my_module as mm
courses = ['History', 'Math', 'Physics', 'CompSci']
index=mm.find_index(courses,'Math')
print(index) #TERMINAL:1

from my_module import find_index
courses = ['History', 'Math', 'Physics', 'CompSci']
index=find_index(courses,'Math')
print(index) #TERMINAL:1

from my_module import find_index,test
courses = ['History', 'Math', 'Physics', 'CompSci']
index=find_index(courses,'Math')
print(index) #TERMINAL:1
print(test)  #TERMINAL:Test String

from my_module import find_index as fi,test
courses = ['History', 'Math', 'Physics', 'CompSci']
index=fi(courses,'Math')
print(index) #TERMINAL:1
print(test)  #TERMINAL:Test String

from my_module import *
courses = ['History', 'Math', 'Physics', 'CompSci']
index=find_index(courses,'Math')
print(index) #TERMINAL:1
print(test)  #TERMINAL:Test String


from my_module import find_index as fi,test
import sys
courses = ['History', 'Math', 'Physics', 'CompSci']
index=fi(courses,'Math')
print(index) #TERMINAL:1
print(test)  #TERMINAL:Test String
print(sys.path) #TERMINAL:['c:\\Users\\ASUS\\Desktop\\Python learning', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']

"""random Library"""
import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_courses=random.choice(courses)
print(random_courses) # TERMINAL:CompSci, Run everytime,will show different courses names in

"""math Library"""
import math
rads=math.radians(90)
print(math.sin(rads)) # TERMINAL:1.0

"""datetime Library"""
import datetime
import calendar
today=datetime.date.today()
print(today) # TERMINAL:2022-03-10

"""leapyear check by calender"""
import calendar
print(calendar.isleap(2017)) # TERMINAL:False

"""import calendar"""
print(calendar.isleap(2020)) # TERMINAL:True

"""Find current working directory"""
import os
print(os.getcwd()) #TERMINAL:C:\Users\ASUS\Desktop\Python learning

"""to show the entire working library directory"""
import os
print(os.__file__) #TERMINAL:C:\Users\ASUS\AppData\Local\Programs\Python\Python39\lib\os.py

""" to understand a library """
import antigravity #It goes to a webbrowser



























