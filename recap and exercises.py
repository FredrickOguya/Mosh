# 🧪 Exercise 1: Basic Abstract Class
# Goal: Create an abstract class Shape with an abstract method area(), then implement two subclasses: Rectangle and Circle.

# 🧩 Step-by-step Instructions:
# Import ABC and abstractmethod from abc.

# Define an abstract class Shape with a method area().

# Create a Rectangle class with width and height.

# Create a Circle class with a radius.

# Both subclasses should implement the area() method.

# Try to instantiate Shape and see the error.

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
        
shapes = [
    Rectangle(4,5),
    Circle(3)
]
 
for shape in shapes:
    print(f"Area: {shape.area()}")
