import math

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius * radius


w = float(input())
h = float(input())
r = float(input())

print(rectangle_area(w, h))
print(circle_area(r))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


rect = Rectangle(w, h)
circle = Circle(r)

print(rect.area())
print(circle.area())
