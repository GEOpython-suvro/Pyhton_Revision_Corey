"""Video 13:   pip - An in-depth look at the package management system
cmd prompt code"""
# pip search pandas------don't run in cmd prompt any more
# pip help install-------will show what to install
# pip list/pip freeze----will show what have been installed already 
# pip install pandas-----will install pandas package
# pip freeze requirements.txt-------will create 'requirements.txt' & show the downloaded packages in requirements.txt

"""Video 14: virtualenv in git bash and why you should use virtual environments"""
# mkdir Environments-----create 'Environments' folder
# cd !$------------------go to 'Environments' folder
# ls---------------------show what are in the folder
# cd..  -----------------comes out of Environment folder
# ls---------------------shows what python learning folder contains
# python -m venv Project1_env----create a new virtual environment called 'Project1_env'
# source Project1_env/Scripts/activate----activate the virtual environment
# which python-----shows under which folder python works
# which pip-----shows under which folder pip works
# pip list------shows the packages and version under 'Project1_env' virtual environment
#  pip install numpy---will install numpy uner 'Project1_env' virtual environment
# pip install pytz---will install pytz under 'Project1_env' virtual environment
# pip freeze -----local> requirements.txt----show all pip install under 'Project1_env' virtual environment
#  cat  requirements.txt---------- shows all pip install under 'Project1_env' virtual environment
#  deactivate---will deactive the 'Project1_env' virtual environment
#  rm -rf Project1_env/-----remove the virtual environment

"""Video 18: Variable Scope - Understanding the LEGB rule and global/nonlocal statements"""
'''LEGB
Local, Enclosing, Global, Built-in
'''
#local variable y within function
x = 'global x'
def test():
    y='local y'
    print(y)
test() # TERMINAL: local y

#Global variable x outside function
x = 'global x'
def test():
    y='local y'
    # print(y)
    print(x)
test() # TERMINAL:global x

#local variable does not print outside function
x = 'global x'
def test():
    y='local y'
    # print(y)
    print(x)
test()
print(y) #TERMINAL:NameError: name 'y' is not defined

#Global variable can print anywhere of the function
x = 'global x'
def test():
    y='local y'
    # print(y)
    print(x)
test()
print(x) #TERMINAL:global x global x

"""local variable always print first and global variable never overwrites function"""
x = 'global x'
def test():
    x='local x'
    # print(y)
    print(x)
test()
print(x) #TERMINAL:local x global x

"""If we want to set a new value for global variable within function"""
x = 'global x'
def test():
    global x
    x='local x'
    # print(y)
    print(x)
test()
print(x) #TERMINAL:local x local x

def test():
    global x
    x='local x'
    # print(y)
    print(x)
test()
print(x)  #TERMINAL:local x local x


def test():
    # global x
    x='local x'
    # print(y)
    print(x)
test()
print(x) #TERMINAL:NameError: name 'x' is not defined

"""Another use of Local variables """
def test(z):
    # global x
    x='local x'
    # print(y)
    print(z)
test('local z') #TERMINAL:local z

def test(z):
    # global x
    x='local x'
    # print(y)
    print(z)
test('local z')
print(z)  #TERMINAL:NameError: name 'z' is not defined

"""Built-in scopes"""
'min' is a builtin function in python
m=min([1,2,3,4])
print(m) 
def test(z):
    x='local x'
    print(z) #TERMINAL:1

"""If we want to see the builtin functions in python, then"""
import builtins
print(dir(builtins))   """TERMINAL: ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 
'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']"""

#Python finds global scope min first and may override with Builtin min function
def min():  #Global min
    pass
m=min([1,2,3,4,5,6,7,8,9])  #Built-in min
print(m) #TERMINAL:TypeError: min() takes 0 positional arguments but 1 was given

#chaged the name of global min into my_min 
def my_min():
    pass
m=min([1,2,3,4,5,6,7,8,9])  #Built-in min
print(m) #TERMINAL:1

#Enclosing scope(Inner scope works first)
def outer():
    x='outer x'
    def inner(): #nested function:function within function
        x='inner x'
        print(x)
    inner()
    print(x)
outer() #TERMINAL:  inner x   outer x

def outer():
    # x='outer x'
    def inner(): #nested function:function within function
        x='inner x'
        print(x)
    inner()
    print(x)
outer()  #TERMINAL:NameError: name 'x' is not defined

def outer():
    x='outer x'
    def inner(): #nested function:function within function
        # x='inner x'
        print(x)
    inner()
    print(x)
outer() #TERMINAL: outer x outer x

def outer():
    x='outer x'
    def inner(): #nested function:function within function
        nonlocal x
        # x='inner x'
        print(x)
    inner()
    print(x)
outer() #TERMINAL:outer x outer x

def outer():
    x='outer x'
    def inner(): #nested function:function within function
        nonlocal x
        x='inner x'
        print(x)
    inner()
    print(x)
outer() #TERMINAL:inner x inner x

x = 'global x'
def outer():
    x='outer x'
    def inner(): #nested function:function within function
        x='inner x'
        print(x)
    inner()
    print(x)
outer()
print(x) #TERMINAL:inner x outer x global x

x = 'global x'
def outer():
    # x='outer x'
    def inner(): #nested function:function within function
        # x='inner x'
        print(x)
    inner()
    print(x)
outer()
print(x) #TERMINAL:global x global x global x

"""An practical example of LEGB scope"""
for a in range(2):
    x = 'global {}'.format(a)
def outer():
    x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)
    def inner():
        x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x) #TERMINAL:inner 3
        print(a, b, c) #TERMINAL:1 2 3
    inner()
    print(x) #TERMINAL:outer 2
    print(a, b) #TERMINAL:1 2
outer()
print(x) #TERMINAL:global 1
print(a) #TERMINAL:1


for a in range(2):
    x = 'global {}'.format(a)
def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)
    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x) #TERMINAL:inner 3
        print(a, b, c) #TERMINAL:1 2 3
    inner()
    print(x) #TERMINAL:outer 2
    print(a, b) #TERMINAL:1 2
outer()
print(x) #TERMINAL:global 1
print(a) #TERMINAL:1

"""Video 19: Slicing Lists and Strings"""
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #      0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    #    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print(my_list[0]) #TERMINAL:0
print(my_list[-10]) #TERMINAL:0
# If I want 1-7
print(my_list[1:8]) #TERMINAL:[1, 2, 3, 4, 5, 6, 7]
print(my_list[-9:-2]) #TERMINAL:[1, 2, 3, 4, 5, 6, 7]
# if want from 2 to the end,9
print(my_list[2:]) #TERMINAL:[2, 3, 4, 5, 6, 7, 8, 9]
#if i want the entire list
print(my_list[:]) #TERMINAL:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[start:end:step]
print(my_list[2:-1:2]) #TERMINAL:[2, 4, 6, 8]
#If I want to reverse step 
print(my_list[-1:2:-2]) #TERMINAL:[9, 7, 5, 3]
#if i want entire list reverse
print(my_list[::-1]) #TERMINAL:[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

sample_url = 'http://coreyms.com'
print(sample_url) #TERMINAL:http://coreyms.com

# Reverse the url
print(sample_url[::-1]) #TERMINAL:moc.smyeroc//:ptth

# # Get the top level domain
print(sample_url[-4:]) #TERMINAL:.com

# # Print the url without the http://
print(sample_url[7:]) #TERMINAL:coreyms.com

# # Print the url without the http:// or the top level domain
print(sample_url[7:-4]) #TERMINAL:coreyms
"""Video 20:Comprehensions - How they work and why you should be using them """
nums = [1,2,3,4,5,6,7,8,9,10]

"""I want 'n' for each 'n' in nums"""
my_list = []
for n in nums:
  my_list.append(n)
print(my_list) #TERMINAL:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#same thing in comprehension
print([n for n in nums]) #TERMINAL:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""I want 'n*n' for each 'n' in nums"""
my_list = []
for n in nums:
  my_list.append(n*n)
print(my_list) #TERMINAL: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# #same thing in comprehension
print([n*n for n in nums]) #TERMINAL:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""I want 'n' for each 'n' in nums if 'n' is even"""
my_list = []
for n in nums:
  if n%2 == 0:
    my_list.append(n)
print(my_list) #TERMINAL:[2, 4, 6, 8, 10]
same thing using list comprehension
my_list = [n for n in nums if n%2 == 0]
print(my_list) #TERMINAL:[2, 4, 6, 8, 10]

"""I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'"""
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter,num))
print(my_list) #TERMINAL:[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]
#same thing using list comprehension
my_list=[(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list) #TERMINAL:[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

"""Dictionary Comprehensions"""
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict) #TERMINAL:{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
#Same thing using dictionary comprehension
my_dict={name:hero for name,hero in zip(names, heros)}
print(my_dict) #TERMINAL:{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
#If name not equal to Peter
my_dict={name:hero for name,hero in zip(names, heros) if name != 'Peter'}
print(my_dict) #TERMINAL:{'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

"""Set Comprehensions"""
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set) #TERMINAL:{1, 2, 3, 4, 5, 6, 7, 8, 9}
##same thing using comprehension
my_set={n for n in nums}
print(my_set) #TERMINAL:{1, 2, 3, 4, 5, 6, 7, 8, 9}

"""Generator Expressions"""
## I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)  
##Same thing using comprehension
my_gen=(n*n for n in nums)
for i in my_gen:
    print(i) #TERMINAL:1 4 9 16 25 36 49 64 81 100

"""Video 21: Sorting Lists, Tuples, and Objects"""
"""Sorting Lists_sorted(li)"""
li = [9,2,6,3,4,6,5,1,8,7]
s_li = sorted(li) #one way of sorted(li) 
print("Sorted Variable:\t", s_li) #TERMINAL:Sorted Variable:         [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
li.sort() #another way of li.sort() 
print("Original Variable:\t",li) #TERMINAL:Original Variable:       [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
#But if we do sort below way, it will return Error
"""li_s = li.sort()
   print("Sorted Variable:\t", li_s")"""

#Sort and Reverse Variable
s_li = sorted(li,reverse=True)
print("Sorted Variable:\t", s_li) #TERMINAL:Sorted Variable:         [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]
li.sort(reverse=True)
print("Original Variable:\t",li)  #TERMINAL:Sorted Variable:         [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]

#Making List of tuples by sorted(tup) tuple
tup=(9,2,6,3,4,6,5,1,8,7)
s_tup = sorted(tup)
print("sorted tuple:\t", s_tup) #TERMINAL:sorted tuple:    [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]

#key of dictionary sorted(dictionary)
di={'name':'John','age':24, 'Likes':['coffee','cake']}
s_di= sorted(sorted(di))
print(s_di) #TERMINAL:['Likes', 'age', 'name']

#absolute value wise sorted()
lis=[-6,-5,-4,2,3,1]
s_lis=sorted(lis,key=abs)
print(s_lis) #TERMINAL:[1, 2, 3, -4, -5, -6]

