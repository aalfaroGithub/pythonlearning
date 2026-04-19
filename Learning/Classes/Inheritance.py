class Animal:
    def eat(self):
        print("Animal eating")

    def sleep(self):
        print("Animal sleeping")

class Pet(Animal):
    # override the method sleep
    def sleep(self):
        print("Pet sleeping")

class Feline:
    def hunt(self):
        print("Feline hunting")

    def purr(self):
        print("Feline purring")

class Dog(Pet):
    pass

class Cat(Pet, Feline):
    # pass
    # def __init__(self) -> None:
    #     super().__init__()

    def __init__(self, name): 
        self.name = name

    def eat(self):
        print(f"Cat {self.name} is eating")
        return super().eat()

print('The dog: ')
dog1 = Dog()
dog1.eat()
dog1.sleep()

# print a blank line
print()
print('The cat: ')

cat1 = Cat('Tommy')
cat1.eat()
cat1.sleep()
cat1.hunt()
cat1.purr()
