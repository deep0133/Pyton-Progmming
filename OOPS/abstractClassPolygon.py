from abc import ABC

#  Wap that has an abstract class polygon derive two classes  rectangle from ploygon and 
# write methods to get the details tf thir dimentsion and find area.

class Polygon(ABC):
    def get_dimensions(self):
        pass
    
    def find_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_dimensions(self):
        return f"Length: {self.length}, Breadth: {self.breadth}"

    def find_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_dimensions(self):
        return f"Base: {self.base}, Height: {self.height}"

    def find_area(self):
        return 0.5 * self.base * self.height

# Creating objects of Rectangle and Triangle classes
rectangle = Rectangle(5, 10)
triangle = Triangle(4, 8)

# Displaying details and area of Rectangle
print("Rectangle Details:")
print(rectangle.get_dimensions())
print("Area:", rectangle.find_area())

# Displaying details and area of Triangle
print("\nTriangle Details:")
print(triangle.get_dimensions())
print("Area:", triangle.find_area())
