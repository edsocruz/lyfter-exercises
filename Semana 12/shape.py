from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    pass

    @abstractclassmethod
    def calculate_perimeter(self):
        pass

    @abstractclassmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return math.pi * 2 * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width




print('\ncircle: ')
circle = Circle(5)
print('Area: ',circle.calculate_area())
print('Perimeter: ',circle.calculate_perimeter())

print('\nsquare: ')
square = Square(5)
print('Area: ',square.calculate_area())
print('Perimeter: ',square.calculate_perimeter())

print('\nrectangle: ')
rectangle = Rectangle(2,5)
print('Area: ',rectangle.calculate_area())
print('Perimeter: ',rectangle.calculate_perimeter())









