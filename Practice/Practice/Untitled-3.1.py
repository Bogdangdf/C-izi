import math

def rectangle_area(a, b):
    return a * b

def circle_area(r):
    return math.pi * r * r


a = float(input())
b = float(input())
r = float(input())

print(rectangle_area(a, b))
print(circle_area(r))


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


rect = Rectangle(a, b)
circle = Circle(r)

print(rect.area())
print(circle.area())
