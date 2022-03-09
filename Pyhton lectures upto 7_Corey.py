#Video lecture 2: String 
greetings = "Hello"
name = "Michael"
print(greetings+", "+ name)
print(len(greetings+", "+ name))
print(name[2])
print(name[-1])
print(name[:4])
print(name[1:3])
my_message="{},{}".format(greetings.upper(), name)

message= "Hello world"
print(message[6:])
print(message.count("l"))
print(message.count("l"))
print(message.find("world"))
print(message.find("universe"))
new_message=message.replace("world","universe")
print(new_message)

#Video lecture 3:  Integers and Floats - Working with Numeric Data 
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
# Less or Equal:    3 <= 2
print(2%2)
print(3%2)
print(4%2)
print(5%2)
print(3*2+1)
num=1
num +=10
print(num)

numb=2
numb*=22
print(numb)

print(abs(-3))
print(round(3.75,1))

num_1 = 3
num_2 =2
print(num_1==num_2)
print(num_1!=num_2)
print(num_1>=num_2)
print(num_1<=num_2)

numb_1="100"
numb_2="200"
numb_1=int(numb_1)
numb_2=int(numb_2)
print(numb_1+numb_2)

#Video lecture 4: Lists, Tuples, and Sets
list_of_courses= ['History','Math','Physics','Compsci']
nums=[1,2,3,4,5]
print(list_of_courses[-1])
print(list_of_courses[:2])
print(list_of_courses[2:])
list_of_courses.insert(0, 'Art')
print(list_of_courses)

courses_2= ['Art','Education']
list_of_courses.extend(courses_2)
print(list_of_courses)

list_of_courses.remove('Math')
print(list_of_courses)

popped=list_of_courses.pop()
print(popped)
print(list_of_courses)

list_of_courses.reverse()
print(list_of_courses)

list_of_courses.sort()
nums.sort()
print(list_of_courses)
print(nums)

list_of_courses.sort(reverse=True)
nums.sort(reverse=True)
print(list_of_courses)
print(nums)

sorted_courses=sorted(list_of_courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(list_of_courses.index('Math'))
print('Math' in list_of_courses)

for item in list_of_courses:
    print(item)

for index, item in enumerate(list_of_courses):
    print(index, item)

for index, item in enumerate(list_of_courses,start=1):
    print(index, item)

list_of_courses_str= ', '.join(list_of_courses)
print(list_of_courses_str)

list_of_courses_str= '- '.join(list_of_courses)
print(list_of_courses_str)

new_list_of_courses=list_of_courses_str.split('-')
print(new_list_of_courses)

#Tuples can't be modified unlike List
#Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#Tuple can't be changed,following is error
tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

#Sets are unordered list if we run the Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'biology'}
print(cs_courses)
print('Math' in cs_courses)

#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Video lecture 5: Dictionaries - Working with Key-Value Pairs
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name':'Suvro','age': 27,'phone':'555-555-5555'})
del student['age']
print(len(student))
print(student.keys())
print(student.items())
for keys in student.keys():
    print(keys)
for key, value in student.items():
    print(key, value)

#Video 6: Conditionals and Booleans - If, Else, and Elif Statements
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

if True:
    print('Conditional was True')
if False:
    print('Conditional was True')

language='pyhton'
if language == 'pyhton':
    print('Language is Python')
else:
    print('No Match')

language='Java'
if language == 'pyhton':
    print('Language is Python')
else:
    print('No Match')

language='Java'
if language == 'pyhton':
    print('Language is Python')
elif language == 'Java': 
    print('Language is Java')  
elif language == 'Javascript': 
    print('Language is Javascript') 
else:
    print('No Match')

# Comparisons
# and 
# or 
# not
user ='Admin'
logged_in = True
if user == 'Admin' and logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials')

user ='Admin'
logged_in = False
if user == 'Admin' and logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials')

user ='Admin'
logged_in = False
if user == 'Admin' or logged_in: 
    print('Admin Page')
else:
    print('Bad Credentials')

user ='Admin'
logged_in = False   
if not logged_in:
    print('Please log in')
else:
    print('Welcome!')

a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7]
print(a==b)
print(a is b)
b=a
print(id(a))
print(id(b))
print(a is b)

# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '', (), [].
#     Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#Video lecture 7: Loops and Iterations - For/While Loops
numeric = [1,2,3,4,5,6,7]
for no in numeric:
    print(no)

#let's find out the number 3 from numeric
numeric = [1,2,3,4,5,6,7]
for no in numeric:
    if no==3:
        print('Found!')
        break
    print(no)

numeric = [1,2,3,4,5,6,7]
for no in numeric:
    if no==3:
        print('Found!')
        continue
    print(no)

numeric = [1,2,3,4,5,6,7]
for no in numeric:
    for letter in 'abc':
        print(no,letter)

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

x=0
while x<10:
    print(x)
    x+=1

x=0
while x<10:
    if x==5:
        break
    print(x)
    x+=1

x=0
while True:
    if x==5:
        break
    print(x)
    x+=1

#to stop the following press ( Ctrl+C)
x=0
while True:
    print(x)
    x+=1




























