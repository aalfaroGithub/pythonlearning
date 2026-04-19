class Circle:

    pi = 3.141592

    # class method
    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)
    
result = Circle.area(14)
print(result) # 615.752192