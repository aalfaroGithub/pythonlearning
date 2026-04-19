# def are first order objects in Python, which means that they can be passed as arguments to other functions, 
# returned as values from other functions, and assigned to variables and stored in data structures.

def centigrade_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

my_funtion = centigrade_to_fahrenheit
print(type(my_funtion)) # <class 'function'>
print(my_funtion(10)) # 50.0

# Lambda functions are small anonymous functions that can have any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
function_grades = lambda grades: grades * 1.8 + 32

print(function_grades(10)) # 50.0

"""
without_params = lambda : True
default_params = lambda a=10, b=20 : a + b
asterisk_params = lambda *args, **kwargs : len(args) + len(kwargs)
"""