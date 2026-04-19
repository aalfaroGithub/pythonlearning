class Number:
    value = 0

    def __init__(self, value):
        self.value = value

    def compare(self, number):
        return max(self.value, number.value)
    
class String:
    value = ""

    def __init__(self, value):
        self.value = value

    def compare(self, string):
        order = [self.value, string.value]
        order.sort()
        return order[0]

class List:
    value = []

    def __init__(self, value):
        self.value = value
        
    def compare(self, list):
        # return max(a,b)
        if len(self.value) > len(list.value):
            return self.value
        return list.value

def return_high_element(a,b):
    return a.compare(b)

number_1 = Number(10)
number_2 = Number(20)

string_1 = String("aaa")
string_2 = String("bbb")

list_1 = List([1,2,3])
list_2 = List([1,2,3,4])

print(return_high_element(number_1, number_2))
print(return_high_element(string_1, string_2))
print(return_high_element(list_1, list_2))
    

### Implementation Whitout polimorphism ###

"""
def return_high_element(a,b):
    # isinstance()
    if isinstance(a, int) and isinstance(b, int):
        return max(a,b)
    if isinstance(a, str) and isinstance(b, str):
        order = [a,b]
        order.sort()
        return order[0]
    if isinstance(a, list) and isinstance(b, list):
        # if len(a) > len(b):
        #     return a
        # return b
        return max(a,b)
    
print(return_high_element([1,2],[1,2,3]))
"""