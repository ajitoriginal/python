# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.

# def changecase(fn):
#     def myinner():
#         return fn().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello Ajit"

# @changecase
# def otherfunction():
#     return "Hello Baby"

# print(myfunction())
# print(otherfunction())

# Arguments in the Decorated Function
# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:
# def changecase(fn):
#     def myinner(name):
#         return fn(name).upper()
#     return myinner

# @changecase
# def anotherfunction(name):
#     return "Hello " + name


# print(anotherfunction('Akshay'))

# *args and **kwargs
# Sometimes the decorator function has no control over the arguments passed from decorated function, 
# to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can 
# accept any number, and any type of arguments, and pass them to the decorated function.

# def changecase(fn):
#     def myinner(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return myinner

# @changecase
# def myfunction(name, lname):
#     return "Hello " + name + " " + lname

# print(myfunction("Anuj", "Singh"))

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.

# def changecase(n):
#     def changecase(func):
#         def myinner():
#             if n == 1:
#                 a = func().lower()
#             else:
#                 a = func().upper()
#             return a
#         return myinner
#     return changecase

# @changecase(2)
# def myfunction():
#     return "Hello Kavi"

# print(myfunction())

# Multiple Decorators
# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.
# def changecase(func):
#     def innerfn():
#         return func().upper()
#     return innerfn

# def addgreeting(func):
#     def innerfn():
#         return "Hello " + func() + " Have a good day"
#     return innerfn

# @changecase
# @addgreeting
# def myfunction():
#     return "Kunal"

# print(myfunction())

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# def myfunction():
#     return "Have a good day"
# print(myfunction())
# print(myfunction.__name__)
# print(myfunction.__doc__)

# But, when a function is decorated, the metadata of the original function is lost.

# def changecase(fn):
#     def myinner():
#         return fn().upper()
#     return myinner

# @changecase
# def myfn():
#     return "Have a nice day"

# print(myfn.__name__)

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
import functools
def changecase(fn):
    @functools.wraps(fn)
    def myinner():
        return fn().upper()
    return myinner

@changecase
def myfn():
    return "Have a nice day"

print(myfn.__name__)