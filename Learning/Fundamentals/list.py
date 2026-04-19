# Lists
# Lists are mutable
# Lists can contain different types
""" (other lists, tuples, dictionaries, sets, strings, numbers, booleans, None, functions, objects, 
    modules, classes, exceptions, files) """
# Create a list
fruits = ['apple', 'banana', 'cherry']
# Access an item
print(fruits[1])
# Change an item
fruits[1] = 'blackberry'
# Add an item
fruits.append('dragonfruit')
# Remove an item
fruits.remove('apple')
# Loop through a list
for fruit in fruits:
    print(fruit)
# Check if an item exists
if 'apple' in fruits:
    print('Yes, apple is in the fruits list')
# Length of a list
print(len(fruits))
# Remove an item by index
fruits.pop(1)
# Other way to remove an item by index
del fruits[1]
# Clear a list
fruits.clear()
# Copy a list
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
# Join two lists
vegetables = ['carrot', 'potato', 'onion']
food = fruits + vegetables
print(food)
# List constructor
fruits = list(('apple', 'banana', 'cherry'))
# Sort a list
fruits.sort() # Ascending order
fruits.sort(reverse=True) # Descending order
# Reverse a list
fruits.reverse()
# Count an item
print(fruits.count('apple'))
# Insert an item
fruits.insert(1, 'blackberry')
# Extend a list
fruits.extend(vegetables)
print(fruits)
# Remove an item by value
fruits.remove('blackberry')
print(fruits)
# Slicing a list, can be posible to get a sublist from a specific to the end with [n:] or 
# from the start to a specific index [:n]
print(fruits[1:3])
# Jumping a specific number of indexes
print(fruits[1:5:2]) # Bring the elements jumping each 2 indexes
# Also [::-1] can be used to reverse the list
# And [:] to copy the list
# Negative indexing
print(fruits[-3:-1])

# List comprehension
# A more concise way to create lists
# Syntax: [expression for item in iterable if condition]
# Example: Create a list containing the squares of the numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Nested lists
# A list can contain other lists
# Example: Create a list containing three lists, each with three items
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_lists)
# Access an item
print(nested_lists[1][2]) # 6
# Loop through a nested list
for inner_list in nested_lists:
    for item in inner_list:
        print(item)

# in and not in operators
# Check if an item exists in a list
if 'apple' in fruits:
    print('Yes, apple is in the fruits list')
if 'apple' not in fruits:
    print('No, apple is not in the fruits list')
    
# List methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value, if not found, an exception is raised
# To avoid the exception, use the in operator
fruits.index('banana') # 1
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
        
# List functions
# all()	Returns True if all items in an iterable are true
# any()	Returns True if any item in an iterable is true
# enumerate()	Takes a collection and returns it as an enumerate object
# filter()	Use a filter function to exclude items in an iterable
# iter()	Returns an iterator object
# len()	Returns the number of items in an object
# max()	Returns the largest item in an iterable
# min()	Returns the smallest item in an iterable
# map()	Returns the specified iterator with the specified function
# reversed()	Returns a reversed iterator
# sorted()	Returns a sorted list
# sum()	Sums the items of an iterator
# zip()	Returns an iterator, from two or more iterators