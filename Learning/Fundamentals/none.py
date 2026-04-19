# Used to represent the absence of a value
# For cases where we don't want to assign a value to a variable
result = None

# Check if a variable is None
if result is None:
    print('No result found')

# None is also a data type
print(type(None)) # <class 'NoneType'>

# None is a singleton
x = None
y = None
print(x is y) # True

# None is falsy
if not result:
    print('No result found')

# None is returned by functions that don't explicitly return a value
def my_func():
    print('Hello')
result = my_func()
print(result) # None

# None is used to represent the absence of a value
# None is not the same as 0, False, or an empty string
# None is a data type of its own (NoneType)
# None is falsy and is returned by functions that don't explicitly return a value
# None is a singleton, meaning that there is only one None

# 8 ways to represent False
# False, None, 0, 0.0, '', [], (), {}
