def operation(amount, balance, operation='deposit'):

    def deposit(amount, balance):
        return amount + balance
    

    def withdraw(amount, balance):
        if amount > balance:
            return 'Insufficient funds'
        return balance - amount
    
    if operation == 'deposit':
        return deposit(amount, balance)
    else:
        return withdraw(amount, balance)

result = operation(10, 30)
print(result) # 40
result = operation(10, 30, 'withdraw')
print(result) # 20