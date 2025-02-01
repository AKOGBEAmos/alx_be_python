# Shapes based objects and areas
import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        return NotImplementedError
    
""" Class Rectacngle is a Shape """
class Rectangle(Shape):
    def __init__(self,length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
""" Circle is also a Shape """
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return (math.pi * math.pow(self.radius, 2))