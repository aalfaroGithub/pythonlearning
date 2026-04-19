age = 20
# if, elif, else
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

# Ternary operator
is_adult = True if age >= 18 else False
print(is_adult)

# variable values with or
t_list = []
name = 'name'

# orvalue = t_list if t_list else name
# If t_list is not empty, orvalue will be t_list, otherwise orvalue will be name
orvalue = t_list or name