# Lazy interators helps to save memory, because we don't need to store all the values in memory, we can get the values one by one

def pairs(): 
    for number in range(0, 10, 2):
        yield number

pairs_result = pairs()

print(next(pairs_result)) # 0

print(next(pairs_result))
print('Ejecuting some code...')
print(next(pairs_result))

while True:
    try:
        print(next(pairs_result))
    except StopIteration:
        print('The generator is empty')
        break