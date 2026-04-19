# Tuples
# Tuples are immutable
# Tuples can contain different types
""" (other lists, tuples, dictionaries, sets, strings, numbers, booleans, None, functions, objects, 
    modules, classes, exceptions, files) """
# Create a tuple
colors = ('red', 'green', 'blue')
# Access an item
print(colors[1])
# Loop through a tuple
for color in colors:
    print(color)
# Check if an item exists
if 'red' in colors:
    print('Yes, red is in the colors tuple')
# Length of a tuple
print(len(colors))
# Tuple constructor
colors = tuple(('red', 'green', 'blue'))
# Count an item
print(colors.count('red'))
# Index of an item
print(colors.index('green'))

# Unpack a tuple
red, green, blue = colors
print(red)
print(green)
print(blue)
# Unpackin number of items with the * operator
# * denotes that the variable is a list
# * -> List
# ** -> Dictionary
# *_ -> Throwaway variable

# Tuple of numbers
numbers = (1, 2, 3, 4, 5)
# Unpack the first two numbers
one, two, *rest = numbers # *rest is a list
# one, two, *_ = numbers # _ is a throwaway variable
# exclude the third and fourth numbers
# one, two, *_, five = numbers
# one, _, *rest, five = numbers
print(one)
print(rest)

# Zip tuples
listN = [1, 2, 3]
tupleN = (4, 5, 6)
zipped = zip(listN, tupleN) # Returns a zip object which is an iterator of tuples, zip can receive n number of iterables
print(zipped)
print(list(zipped)) # Convert the zip object to a list of pairs of tuples [(1, 4), (2, 5), (3, 6)]
print(tuple(zipped)) # Convert the zip object to a tuple of pairs of tuples ((1, 4), (2, 5), (3, 6))


# Join two tuples
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'potato', 'onion')
food = fruits + vegetables
print(food)
# Slicing a tuple
print(fruits[1:3])
# Negative indexing
print(fruits[-3:-1])

# Convert a tuple to a list
colors_list = list(colors)
print(colors_list)
# Convert a list to a tuple
colors_tuple = tuple(colors_list)
print(colors_tuple)