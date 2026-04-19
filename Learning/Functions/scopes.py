# Scope
animal = 'turtle' # global scope (can be accessed anywhere in the file)

def print_animal():
    # To use the global variable inside the function, it´s necessary to use the keyword global
    # Adding global, if we modify the variable inside the function, it will be modified in the global scope
    global animal

    animal = 'snake' # local scope
    print(animal) # snake
    # animal is a local variable and it´s not the same as the global variable animal
    print(id(animal)) 

    animal_type = 'reptile' # local scope

    def second_level():
        nonlocal animal_type # nonlocal keyword is used to work with the variable in the outer enclosing scope
        animal_type = 'mammal' # nonlocal scope

print_animal()
print(animal) # turtle
print(id(animal))