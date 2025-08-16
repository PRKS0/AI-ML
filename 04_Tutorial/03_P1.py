class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def summary(self):
        print(f'My name is {self.name}, roll number is {self.roll} and I live in {self.address}')
    

nos = int(input("Enter number of student: "))
obj_list = []

for i in range(nos):
    name = input("Name: ")
    roll = input("Roll: ")
    address = input("Address: ")

    obj_list.append(Student(name, roll, address))

for i in obj_list:
    i.summary()
