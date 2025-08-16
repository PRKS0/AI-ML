# This is comment
# a = 12
# b = "name"
# c = 12.45

# basic data type 
# print(type(a))
# print(type(b))
# print(type(c))

# # basic type conversion
# d = str(a)
# e = int(c)

# print(d)
# print(type(d))
# print(e)
# print(type(e))


# # Python allows you to assign values to multiple variables in one line
# name, age, gender = "prakash", "19", "Male"
# print(name, age, gender)

# # extracting value from list
# fruits = ["apple", "banana", "mango"]
# app, bana, man = fruits
# print(app, bana, man)


# Global Variable

# profile = "Prakash"
# def myFunc():
#     print(profile)
#     global profile

# myFunc()


# datatype
# x = "prakash"
# # print(x[1])
# for i in x:
#     print(i)

a = "my name is prakash, and I am from"
# print(a.strip())
# print(a.replace("prakash", "tanka"))
# print(type(a.split(",")))

# formating string
# ab = a + " Jajarkot"
# ab = f"{a} Jajarkot. And I love my village"
# price = "50$"
# ab = f"price of my new table is {price} and I am happy with that"


# ab = "My name is \"prakash\" "
# ab = "hello world! \r my name is prakash"
# print(ab)
# I dont get this \r 
# ab = "prakash budha chhetri"
# print(ab.format())
# print(ab)

# print(bool(0))

# def myFunction() :
#   return False

# print(myFunction())

# a = 20000
# print(isinstance(a, int))

# a = "100"
# b = "1"
# print(a and b)

# thislist = ["apple", "banana", "cherry"]

# # thislist[0:2] = ["blackcurrant", "banana2", "banana3"]
# thislist.insert(3, "apple2")

# print(thislist)

list1 = ["apple", "banana", "cherry"]
# list1.remove("apple")
# del list1[2]
# del list1
# list1.clear()
# print(list1)

# for x in list1:
#     print(x)

# for i in range(len(list1)):
#     print(list1[i])

# [print(x) for x in list1]

# list2 = []

# for item in list1:
#     if "e" in item:
#         list2.append(item)

# print(list2)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "bamana" ]
# thislist.sort(reverse=True)
# print(thislist)


# def myFunc(n):
#     return abs(n-10)

# random_num = [12, 3, 20, 90, 34, 0, 15]
# random_num.sort(key = myFunc)
# print(random_num)

# Day-2

# fruits = ("apple", "banana", "cherry")
# f1, f2, f3 = fruits
# print(f1)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# print(fruits.count("apple"))

# s = {("bool", False), ("int", 0)}
# # print(s)

# fruits = {"apple", "banana", "mango"}
# fruits.add("mango")
# fruits.add("Mango")
# fruits.add("orange")
# fruitsss = sorted(fruits)
# print(fruitsss)
# print(type(fruitsss))
# print(fruits)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# car.update({"sells": 200})
# car["color"] = "blue"
# print(car)

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# print(car)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child1"]["year"])

# def adder(a, b, /):
#     print(a)
#     print(b)

# adder(2, 1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # def __str__(self):
#     #     return f"hello, my name is {self.name} and I am {self.barsa} years old."

#     def printName(self):
#         print(f"My name is {self.name} and I am {self.age} years old")

# person1 = Person('Prakash', 19)
# person1.printName()


# class VIP(Person):
#     def __init__(self, name, age, post, security):
#         super().__init__(name, age)
#         self.post = post
#         self.security = security

#     def printer(self):
#         print(f"{self.name} is {self.post} with {self.security} security")
    

# VIP("rajesh", 20, "MP", 1200).printName()
# VIP("rajesh", 20, "MP", 1200).printer()

# import file1

# file1.namaste("prakash")

# import platform
# x = platform.system()
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x)

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)