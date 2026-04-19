# New class representing a person
# ClassName always in CamelCase and in singular
class Person:
    # Class Attrs are the properties of the class
    # Instance Attrs are the properties of the instance of the class

    # Class Attr
    person_name = ''
    person_email = ''
    # By convention _attr is a private attribute
    # __attr is a private attribute that cannot be accessed directly, only through a method, or by using object._ClassName__attr, 
    # also they are not inherited

    # private property for the height
    __height = 0

    # Constructor method
    def __init__(self, name, age):
        # Adding attributes to the object
        self.name = name
        self.age = age
    
    def add_person_email(self, email):
        self.email = email

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    # Defining the getter and setter for the private attribute
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError('Height cannot be negative')
        self.__height = height

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
person1 = Person('John', 25)
person2 = Person('Marta', 24)

person1.add_person_email('test1@gmail.com')
person2.add_person_email('test2@gmail.com')

print(person1.__dict__)
print(person2.__dict__)