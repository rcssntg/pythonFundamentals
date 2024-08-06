# # Welcome Message
# greeting = 'Hello'
# name = 'Michael'

# # message = greeting + ', ' + name + '. Welcome!'

# #message = f'{greeting}, {name.upper()}. Welcome!'

# print(help(str.lower))


# num = 3.1

# print(type(num))

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication    3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

# Comparison:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
    

# num = 1
# # num = num + 1
# num *= 10


# num_1 = 3
# num_2 = 2

# print(num_1 <= num_2)



# num_1 = '100'
# num_2 = '200'

# num_1 = int(num_1)
# num_2 = int(num_2)

# print(num_1 + num_2)

# List, Tuple and sets

# courses = ['History', 'Math', 'Physics', 'Compsci']
# nums = [1, 5, 2, 4, 3]

# sorted_courses = sorted(courses)

 

# print('Math' in courses)


# A LIST is Mutable
# A TUPLE is Immutable

# student = {'name': 'John', 'age': 25, 'course': ['Math, Compsci']}

# print(student.get('phone', 'Not Found'))


# conditionals and booleans

# language = 'Javascript'

# if language == 'Python':
#     print('Language is Python')
# elif language == 'Javascript':
#     print('Language is Javascript')
# else:
#     print('No match')

# user = 'Admin'
# logged_in = True

# if not logged_in:
#     print('Please Log In')
# else:
#     print('Welcome')

# LOOPS AND ITERATIONS
# nums =[1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found it!')
#         continue
#     print(num)

# for num in nums:
#     for letter in 'rcs':
#         print(num, letter)


# x = 0

# while True:
#     print(x)
#     x += 1

# FUNCTIONS

# def hello_func():
#     print('Hello Ronel...')
    
# hello_func()
# hello_func()
# hello_func()
# hello_func()

# DRY - Don't Repeat Yourself

# def hello_func(greeting, name='You'):
#     return '{}, {}'.format(greeting, name)

# print(hello_func('Hi', name = 'Ronel'))

# from my_module import find_index, test
# import sys

# courses = ['History', 'Math', 'Physics', 'Compsci']

# index = find_index(courses, 'Math')
# # print(index)
# # print(test)

# print(sys.path)


# PYTHON OBJECT ORIENTED PROGRAMMING


class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Ronel', 'Santiago', 45000)
emp_2 = Employee('Jennifer', 'Santiago', 30000)
emp_3 = Employee('Sophia', 'Santiago', 10000)
emp_4 = Employee('Samantha', 'Santiago', 9000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

print(Employee.num_of_emps)








