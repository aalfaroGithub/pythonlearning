def sum(n1, n2): 
    # return can return multiple values
    return n1 + n2, 'The sum of the numbers is: ' + str(n1 + n2)

num1 =  int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result, message = sum(num1, num2) # result is a tuple
print(result)
print(message)

