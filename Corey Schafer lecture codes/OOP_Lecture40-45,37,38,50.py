
"""what's learn first class functions and its Properties?
 
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists..."""

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg)) #'<{0}>{1}</{0}>';tag=0;msg=1
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!') #TERMINAL:<h1>Test Headline!</h1>
print_h1('Another Headline!') #TERMINAL:<h1>Another Headline!</h1>

print_p = html_tag('p')
print_p('Test Paragraph!') #TERMINAL:<p>Test Paragraph!</p>

"""What is closure? Ans: Closures allow us to take advantage of first class functions and return an inner functions that remembers and has access to variables local to the scope they were created"""

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args): #'*args' means we cn pass in any no of arguments to this function 
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10) #TERMINAL:6  9  5  10

"""Video 40: OOP_Classes and Instances"""
"""Instance variables are unique while class variables are shared among all instances of a class"""
"""create an application for company with the employees and python code using simple Employee class"""
class Employee: #classe is a blueprint for creating instances
    
    def __init__(self, first,last,pay): #init method.Inside method,by convention,instance=self.other arguments-first,last,pay
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first+'.'+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
emp_1= Employee('Corey','Schafar',50000) #emp_1 is a unique instance variable of Employee class.
emp_2= Employee('Test','user',60000)  #emp_2 is a unique instance variable of Employee class
print(emp_1.fullname()) #TERMINAL:Corey Schafar
print(emp_1.email) #TERMINAL:Corey.Schafar@company.com
print(Employee.fullname(emp_1)) #TERMINAL:Corey Schafar

"""Video 41:Class Variables"""
class Employee:
    raise_amt = 1.04  #it's a Class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.__dict__) #TERMINAL:{'first': 'Corey', 'last': 'Schafer', 'email': 'Corey.Schafer@email.com', 'pay': 50000}
print(emp_1.pay) #TERMINAL:50000    ;Pay before apply_raise
emp_1.apply_raise()
print(emp_1.pay) #TERMINAL:52000    ;Pay after apply_raise


""" If we change instance raise amount,it can't change class raise amount"""
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.raise_amt =1.05
print(Employee.raise_amt) #TERMINAL:1.04
print(emp_1.raise_amt) #TERMINAL:1.05
print(emp_2.raise_amt) #TERMINAL:1.04



"""If we change class raise amount,it changes raise amount for class,instances"""
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.raise_amt =1.05
print(Employee.raise_amt) #TERMINAL:1.05
print(emp_1.raise_amt) #TERMINAL:1.05
print(emp_2.raise_amt) #TERMINAL:1.05


"""keep tracking of employees"""
class Employee:
    raise_amt = 1.04 
    num_of_emps = 0 #it's also class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1 # with the raises its nice to have constant class value that can be overridden per instance
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
print(Employee.num_of_emps) #TERMINAL:0    ;before any instance employee
emp_1 = Employee('Corey', 'Schafer', 50000) #instance employee 1
emp_2 = Employee('Test', 'Employee', 60000) #instance employee 2
print(Employee.num_of_emps) #TERMINAL:2     ;after two instance employees


"""Video 42: regular methods vs class methods vs static(instance) methods"""
"""A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method cant access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python."""
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt) #TERMINAL:1.05
print(emp_1.raise_amt)#TERMINAL:1.05
print(emp_2.raise_amt)#TERMINAL:1.05

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email) #TERMINAL:John.Doe@email.com
print(new_emp_1.pay) #TERMINAL:70000

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date)) #TERMINAL:True

"""Video 43: Inheritance - Creating Subclasses"""
"""Inherit allows us to inherit attributes & methods from parent class"""
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email) #TERMINAL:Sue.Smith@email.com

mgr_1.print_emps() #TERMINAL: --> Corey Schafer

"""Video 44:Special (Magic/Dunder) Methods"""
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2) #TERMINAL:110000

print(len(emp_1)) #TERMINAL:13


"""Video 45:Property Decorators - Getters, Setters, and Deleters"""
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first) #TERMINAL:Corey
print(emp_1.email) #TERMINAL:Corey.Schafer@email.com
print(emp_1.fullname) #TERMINAL:Corey Schafer

del emp_1.fullname #TERMINAL:Delete Name!