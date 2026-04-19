average = lambda *args: sum(args) / len(args)

aproved = lambda calification: calification >= 7

def show_message(func_average, func_aproved, *args):
    average_result = func_average(*args)

    if func_aproved(average_result):
        return f'Congrats, you aproved with an average of: {average_result}'
    else:
        return 'Student disapproved'

print(show_message(average, aproved, 10, 8, 9, 7, 6)) # Congrats, you aproved with an average of: 8.0


# Returning a function

def say_hi():

    def show_message():
        print('Hi, this is a nested function')

    return show_message

response = say_hi()

response() # Hi, this is a nested function