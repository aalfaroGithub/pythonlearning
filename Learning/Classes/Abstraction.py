from abc import ABC, abstractmethod # Abstract Base Class
# from Abstraction import Hash, Queue

# All abstract class must inherit from ABC
class Structure(ABC):
    @abstractmethod
    def get_row(self, key):
        pass
    
    @abstractmethod
    def add_row(self, key, value):
        pass

class Hash(Structure):
    row = {}

    def get_row(self, key):
        return self.row[key]
    
    def add_row(self, key, value):
        self.row[key] = value
        return self.row[key]
    
class Queue(Structure): 
    row = []
    
    def get_row(self, key):
        return self.row[0]
    
    def add_row(self, key, value):
        self.row.append(value)
        return self.row[-1]
    
class BankRow:
    def __init__(self, users_row):
        if not isinstance(users_row, Structure):
            raise TypeError("users_row must be a Structure")
        
        self.users_row = Queue()
    
    def get_next_user(self, key):
        return self.users_row.get_row(key)
    
    def add_user_to_the_row(self, user):
        return self.users_row.add_row(user['id'], user)
    

bank_row = BankRow([])

user = {
    "id": 1,
    "name": "John"
}

bank_row.add_user_to_the_row(user)