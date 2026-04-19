############################################
# Optional arguments
############################################
def circle_area(radius, pi=3.14):
    return pi * (radius ** 2)

print(circle_area(5)) # 78.5
# It´s possible to change the default value
print(circle_area(5, 3.1416)) # 78.54
# It´s possible to change the order of the arguments using the name of the argument
print(circle_area(pi=3.1416, radius=5)) # 78.54

############################################
# Arguments
"""
*args: It´s a tuple that allows to pass a variable number of arguments to a function
Also it's possible to receive some paramenters and then use *args and **kwargs
def average(p1, p2, *args, p4=200):
p1 = 10, p2 = 20, args = (30, 40, 50)
average(10, 20, 30, 40, 50, p4=400) 
"""
############################################
def average(*args):
    print(args) # (10, 20, 30, 40, 50
    print(type(args)) # <class 'tuple'>
    return sum(args) / len(args)

average_result = average(10, 20, 30, 40, 50)
print(average_result) # 30.0
