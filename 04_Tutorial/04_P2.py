class Animal:
    def speak(self):
        print("Animal is making sound")
    
class Dog(Animal):
    def speak(self):
        print("Bark !")

class Cat(Animal):
    def speak(self):
        print("Meow !")

class Parrot(Animal):
    def __init__(self, sound):
        self.sound = sound
    def speak(self):
        print(f'{self.sound} !')

message = input("Message: ")
zoo = [Dog(), Cat(), Parrot(message)]


for animal in zoo:
    animal.speak()