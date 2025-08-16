# 🧩 Problem 3: Shape Area Calculator
# Concepts: Abstract base class (optional), polymorphism

# Create a base class Shape with:

# A method area() that raises NotImplementedError

# Then create subclasses:

# Circle with radius and formula for area

# Rectangle with length and breadth and its area

# Make a list of different shape objects and print their areas using a loop.

# Bonus Twist: Use the abc module to make Shape an abstract class. (Optional)

# Goal: Get comfy with polymorphism and design thinking using inheritance.


import math

class Shape:
    def area(self):
        return 0  # Default, could also raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Create a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(10, 2)
]

# Loop through and print area of each
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
