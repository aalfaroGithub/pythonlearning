"""
Print some text to the console
# Run this script by typing 'python main.py' in the terminal
"""
print('Test Python Script!')

# variables
language_course = 'Python'
# constants, on python we use all caps for constants
PI = 3.14159

# Data types
# String
name = 'John Doe'
# For breaklines we use triple quotes
address = '''123 Main St
Some City, Some State
12345'''
# Integer
age = 30
# Float
height = 1.75
# Dividing two integers will return a float but using // will return an integer
result_of_division = 10 // 3
# Boolean (True or False)
is_married = False

# Variables in one line
name, age, height = 'Jane Doe', 25, 1.65

# Dynamic typing (Python is a dynamically typed language)
dinamic_type = 10
print(dinamic_type)
dinamic_type = 'Hello'
print(dinamic_type)

# Type casting
# str()
age_str = str(age)
# int()
height_int = int(height)
# float()
age_float = float(age)

# Type checking
print(type(name))
print(type(age))
print(type(height))

# <, > , <=, >=, ==, !=
# and, or, not