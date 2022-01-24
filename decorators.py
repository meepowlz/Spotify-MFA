# """
# Serves as an example for how function decorators work
# To aid in creating decorators for login purposes
# """
#
#
# # Cheese is the decorator
# def cheese(function):  # do_math is passed into cheese here
#     def wrapper(x, y):  # the x and y arguments from do_math are accessed by wrapper
#         print("Starting value: x=" + str(x) + " y=" + str(y))
#         result = function(x, y)  # now do_math is called
#         print("After function!")
#         print("Result: " + str(result))
#
#     return wrapper
#
#
# @cheese
# # do_math is passed into cheese as an argument
# def do_math(x, y):  # x and y passed as arguments
#     print("I'm running!")
#     print(str(x) + " is multiplied by " + str(y))
#     result = x*y
#     return result
#
#
# do_math(4, 7)
