# Lambda Functions
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:

# x = lambda a: a + 10
# print(x(10))

# x = lambda a, b: a + b
# print(x(10, 20))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# Or, use the same function definition to make both functions, in the same program:

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.

# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()
# The map() function applies a function to every item in an iterable:

# numbers = [1,2,3,4,5]
# doubled = list(map(lambda x : x * 2, numbers))
# print(doubled)

# Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)

# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:


# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


