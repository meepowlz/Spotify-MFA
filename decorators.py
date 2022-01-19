"""
Serves as an example for how function decorators work
To aid in creating decorators for login purposes
"""


# Making sense of decorators
def cheese(function):
    def wrapper():
        print("Before the function")
        function()
        print("After function!")
    return wrapper


@cheese
def our_function():
    print("I'm running!")

our_function()
