# Strings 
# Strings are immutable, meaning they cannot be changed after they are created

# split example
cars = "audi bmw subaru toyota"
cars_list = cars.split() # Split by default splits by space
# Delimiter .split(",")
# Limit .split(",", 2), return a list with 2 elements and the rest of the string
 
# Join example
# List of strings
words = ['Coding', 'is', 'fun']
# Join the list of strings into a single string
sentence = ' '.join(words) # Join with a space between each word

# String formatting
# Old way
name = 'John'
middle_name = 'Doe'
complete_name = name + ' ' + middle_name
age = 30
print('My name is %s and I am %d years old' % (name, age))
# New way
print('My name is {} and I am {} years old'.format(name, age))
# Format with parameters
print('My name is {name} and I am {age} years old'.format(name=name, age=age))
# f-strings
print(f'My name is {name} and I am {age} years old')

# count of in helps us to know how many times a substring appears in a string
# word in String returns True if the word is in the string

# String methods
# capitalize
print(complete_name.capitalize())
# upper
print(complete_name.upper())
# lower
print(complete_name.lower())
# swapcase
print(complete_name.swapcase())
# title
print(complete_name.title())
# replace
print(complete_name.replace('John', 'Jane'))
# count (count the number of occurrences of a substring)
print(complete_name.count('o'))
# startswith
print(complete_name.startswith('John'))
# endswith
print(complete_name.endswith('Doe'))
# split
print(cars_list)
# join
print(sentence)
# find (returns the index of the first occurrence of the substring)
print(complete_name.find('Doe'))
# len
print(len(complete_name))
# strip (removes any whitespace from the beginning or the end)
print(complete_name.strip())
# lstrip (removes any whitespace from the beginning)
print(complete_name.lstrip())
# rstrip (removes any whitespace from the end)
print(complete_name.rstrip())
# isalnum (returns True if all characters are alphanumeric)
print(complete_name.isalnum())
# isalpha (returns True if all characters are alphabetic)
print(complete_name.isalpha())
# isnumeric (returns True if all characters are numeric)
print(complete_name.isnumeric())
# islower (returns True if all characters are in lower case)
print(complete_name.islower())
# isupper (returns True if all characters are in upper case)
print(complete_name.isupper())
# istitle (returns True if the string follows the rules of a title)
print(complete_name.istitle())
# isspace (returns True if all characters are whitespace)
print(complete_name.isspace())



