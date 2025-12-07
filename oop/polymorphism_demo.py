# polymorphism_demo.py
import math
class Shape():
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

class Rectangle(Shape):
    """ Rectangl shape derived from shape ."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle """
        return self.length * self.width

class Circle(Shape):
    """ Circle shape derived from shape. """
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2 )