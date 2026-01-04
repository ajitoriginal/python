import sys
import random
# print("Hello, Ajit!")
# print(sys.version)
# print("first"); print("second")

# print("first", end=" "); print("second")
# print(3)
# print(4+5)
# print(3-1)
# print("I am", 29, "years old.")
# """
# This is
# a multi-line
# comment
# """

# x = 5
# y = "test"
# print(x)
# print(y)

# casting
# x = str(3)
# # y = int(3)
# # z = float(3)
# # m = 3
# # X = 5
# print(type(x), x, type(y), y, type(z), z, type(m), m, X)
# x, y, z = "Ajit", "Bruce", "Super"
# x, y, z = ["Ajit", "Bruce", "Super"]
# names = ["Ajit", "Bruce", "Super"]
# x, y, z = names
# x = y = z = "Ajit"
# y = "Singh"
# print(x, y, z)
# x = 5
# y = "Ajit"
# print(x,  y)
# print(x)

# x = "Ajit is awesome"
# def myFunc():
#     global x
#     x = "new value"
#     print(x)
# myFunc()
# print(x)
# y = 'redmagic'
# print(random.randrange(1, 10))
# for x in "banana":
#     print(x)
# print(len(y))

# text = "Ajit is the best person"
# print("best" in text)
# for x in text:
#     print(x)


# if "bestd" not in text:
#     print("yes")
# else:
#     print("no")

# b = "Hello Ajit"
# c = "Hello Ajit "
# n = "Hello,Guys"
# print(b[-4:-1])
# print(b.upper()) 
# print(b.lower()) 
# print(c.strip()) 
# print(c.replace("H", "K"))
# print(n.split(","))
# age = 29
# txt = f"My name is AJit, I am {10 + age:.3f}"
# print(txt)

# txt = "this is a t\"ext s\\tri\n\\g"
# print(txt)
# x = "trimaxma ma"
# y = "Trimaxma"
# print(x)
# print(x.capitalize())
# print(y.casefold())
# print(x.center(10))
# print(y.count("ma"))
# print(y.find("m"))
# print(x.title())

# thisList = ["apple", "banana", "cherry", "banana"]
# print(thisList)
# print(len(thisList))
# print(type(thisList))
# newList = list(("banana", "cherry", "banana", "apple", "guava", "amla"))
# print(newList)
# print(len(newList))
# print(type(newList))
# print(newList[1])
# print(newList[-1])
# print(newList[2:5])
# print(newList[:4])
# print(newList[2:])
# print(len(newList[2:]))
# print(newList[-4:-1])
# if "amla" in newList:
#     print("yes amla is in the newList")

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# [print(x) for x in thislist]

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = [x for x in fruits if "a" in x]
# print(newList)
# newlist2 = [x.upper() for x in fruits]
# print(newlist2)
# newlist3 = ['hello' for x in fruits]
# print(newlist3)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# thislist.sort(reverse = True)
# print(thislist)
# mylist = thislist.copy()
# mylist = list(thislist)
# mylist= thislist[:]
# print(mylist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
# for x in list2:
#     list1.append(x)
list1.extend(list2)
print(list1)



