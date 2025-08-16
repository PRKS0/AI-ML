# __attribute = make this attribute private for some reasons
# (getter) get_attribute = make that private attribute accessible using get_attribute method (getter) (can modify the value of __attribute)
# (setter) set_attribute = we make attribute private, now we can't change it's value, so we make a function/method which change the value of private attribute

class Chai:
    def __init__(self, tea, sugar):
        self.__tea = tea
        self.sugar = sugar

    # getter
    def get_tea(self):
        return self.__tea
    
    # setter
    def set_age(self, new_tea):
        self.__tea = new_tea
        # if isinstance(new_tea, str):
        #     self.__tea = new_tea
        # else:
        #     print("Invalid name: must be a string")

me_chai = Chai('10gm', '20gm')
print(me_chai.get_tea())
me_chai.set_age('8gm')
print(me_chai.get_tea())



# staticmethod = we want a function which is standalone inside class. no need of giving self parameter (can give other required parameters). therefore can't access instance state (attribute of object), and also class level attribute. That means it has no connection with object and even class. it is just inside class. but it can be called using class and object both. (it is decorator in python)

class Home:
    location = "kathmandu"

    def __init__(self, room, storey):
        self.room = room
        self.storey = storey

    @staticmethod
    def define_home():
        # can't access self.room and self.storey    (instance state)
        # can't access loation                        (class state)
        return "A place where one lives; a residence"

home1 = Home(5, 1)
print(home1.define_home())              # can also pass arguments, and use on function defination
print(Home.define_home())



# property: simply property is used to use/call the method as attribute/property. (no need to use obj.method(), only obj.method). this decorator convert method into property. Use: when we make attribute private, it can't be both read and write through object. but what if we want to make it only readable. we use decorator called property.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

p1 = Person("darshan", 16)
print(p1.age)
# print(p1.age())           :error




# isinstance: return boolean value on checking whether given object is of given class or not
class Building:
    desc = "I am building a building"

home = Building()
print(isinstance(home, Building))