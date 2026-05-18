
import math

class Circle:
    def __init__(self):
        self.radius = 0
    def area(self):
        return (math.pi * self.radius**2)

class Square():
    def __init__(self):
        self.side = 0
    def area(self):
        return (self.side**2)

class Rectangle():
    def __init__(self):
        self.base = 0
        self.height = 0
    def area(self):
        return (self.base*self.height)

def largest_area (a, b, c):
    max_value = max(a.area(), b.area(), c.area())
    print('Largest area = ', max_value)
