# Recolect the input data from the user
input_name = input("Enter your name: ")
input_age = input("Enter your age: ")

print(type(input_age))
int_age = int(input_age)
print(type(int_age))

# No es buena practica convertir ints a strings, pero es posible
str_age = str(int_age)

authorization = input("Are you authorized? (yes/no): ") == 'yes'
print(authorization)

print(f"Hello {input_name}, you are {int_age} years old. Authorized")