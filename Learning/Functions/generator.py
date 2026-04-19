# Generators
# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# generator function
# Lazy iterator
def pairs(): 
    for number in range(0, 100, 2):
        # If we use return, the function will return the first value and finish the execution
        yield number # yield is a keyword that is used like return, but it returns a generator

pairs_result = pairs()
# Using next to get the next value
print(next(pairs_result)) # 0

print('some text')

# the generator is an iterator, so we can use the next function to get the next value, we get the values one by one
for pair in pairs_result:
    print(pair)

# Yield suspends the function and sends a value back to the caller, 
# but retains enough state to enable the function to resume from where it is left off in the next call.