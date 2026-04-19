# A closure is a function object that has access to variables in its enclosing scope, even after the scope has finished executing.
def say_hi(username):
    message = f'Hi {username}' # local scope

    def show_message():
        print(message)

    return show_message

username = 'User1'
response = say_hi(username)
username = 'User2'


response() # Hi User1
response() # Hi User1
response() # Hi User1