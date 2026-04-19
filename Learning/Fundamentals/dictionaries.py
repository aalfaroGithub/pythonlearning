# Dictionary
# Dictionaries are mutable, unordered collections of items. They have a key-value pair.
# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Create a dictionary
# Also with the dict() constructor
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'is_married': False,
    'hobbies': ['reading', 'music', 'movies'],
    'address': {
        'street': '123 Main St',
        'city': 'Some City',
        'state': 'Some State'
    }
}

# Access an item
print(person['first_name'])
# Get method
print(person.get('last_name'))
other_field_list = person.get('other_field', [])
if other_field_list:
    for field in other_field_list:
        print(field)
# if the key does not exist, it will return None

# Set default value
# If the key does not exist, it will added with the default value
value = person.setdefault('other_field', "This is the default value")



# Add an item
person['phone'] = '555-555-5555'

# Get keys
print(person.keys())
# Convert to tuple to make it immutable, (read-only)
keys = tuple(person.keys())
print(keys)
# Get values
dict_values = tuple(person.values())
print(dict_values)
# Get items
dic_items = tuple(person.items())
print(dic_items)

# Copy a dictionary
person2 = person.copy()
person2['city'] = 'Another City'
print(person2)

# Remove an item
if 'age' in person:
    del person['age']
if 'phone' in person:
    phone = person.pop('phone')
print(person)

# Clear a dictionary
person.clear()
print(person)

# Length of a dictionary
print(len(person2))

# List of dictionaries
people = [
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 25}
]
print(people[1]['name'])

# Dictionary constructor
person = dict(first_name='John', last_name='Doe')
print(person)

# Check if a key exists
print('first_name' in person)
print('last_name' not in person)

# Update a dictionary
person.update({'first_name': 'Jane', 'age': 25})
print(person)

# Loop through a dictionary
for key, value in person.items():
    print(key, value)

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# comprehension
# Create a dictionary from a list
names = ['John', 'Jane', 'Joe']
names_dict = { user: position + 1 for position, user in enumerate(names) }
print(names_dict)