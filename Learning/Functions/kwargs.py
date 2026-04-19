############################################
# Arguments
"""
**kwargs: It´s a dictionary that allows to pass a variable number of arguments to a function
"""
############################################
def users (**kwargs):
    print(kwargs) # {'name': 'John', 'age': 30, 'city': 'New York'}
    print(type(kwargs)) # <class 'dict'>


def combiantion(*args, **kwargs):
    print(args) 
    print(kwargs)
    print(type(args)) # <class 'tuple'>
    print(type(kwargs)) # <class 'dict'>


users(John=[10,10,9], kale=[10,9,10])
combiantion(10, 20, 30, 40, 50, name='John', age=30, city='New York')