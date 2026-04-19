"""
Decorators are a way to modify the behavior of a function without changing its code.
A decorator is a function that takes another function as an argument and adds some kind of functionality to it.
The @ symbol is used to apply the decorator to the function being defined.

a -> main function (decorator)
b -> function to be decorated
c -> decorated function

a(b) -> c
"""

def function_a(function_b):

    def function_c(*args, **kwargs):
        print('This is the first line of the decorator')
        result = function_b(*args, **kwargs)
        print('This is the last line of the decorator')

        return result

    return function_c

# @function_a
# def say_hello():
#     print('Hello!')

@function_a
def sum(a=10, b=30):
    return a + b

# say_hello() 
result = sum()
print(result)