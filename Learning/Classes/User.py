class User:
    # Class Attr
    username = 'Default username'
    email = ''

    # Instance Attr
    # Can be added dinamically
    # They belongs to each object of the class

# __dict__ is a special attribute that returns a dictionary containing a class's namespace
# 1. Check if the attr exists inside the object
# 2. If not, check if the attr exists inside the class -> Only for read access, can't modify the class attr
# 3. If not found on either, raise an AttributeError

user1 = User() 
user1.username = 'JohnDoe' # This will create a new instance attr to the object
# This will create a new instance attr to the object
# user1.password = '12345' 
print(user1.username)

# printing the id of the object
print(id(user1.username))
print(id(User.username)) 

print(user1.__dict__) # Dict
    
