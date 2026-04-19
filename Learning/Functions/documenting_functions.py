# Docstring
# __doc__ (Module, Class, Function, Method)
def sum(a, b):
    """
    This function takes two arguments, a and b, and returns their sum.

    Arguments:
    a: int
    b: int

    Returns:
    Sum of a and b

    >>> sum(1, 2)
    3

    TODO:
    - Add type hints
    - Add support for floats
    - Some other thing
    """
    return a + b

print(sum.__doc__)
# Or 
print(help(sum))

# Docstring for testing
# adding >>> calling the function with the params
# adding ... the expected result in the next line
# And in the console run:
# python -m doctest -v Functions/documenting_functions.py