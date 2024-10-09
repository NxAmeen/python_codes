from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def _init_(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        return self.length * self.breadth
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

def main():
    print("Select a shape:")
    print("1. Circle")
    print("2. Rectangle")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        shape = Circle(radius)
        print("Circle Area:", shape.calculate_area())
        print("Circle Perimeter:", shape.calculate_perimeter())
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        shape = Rectangle(length, breadth)
        print("Rectangle Area:", shape.calculate_area())
        print("Rectangle Perimeter:", shape.calculate_perimeter())
    else:
        print("Invalid choice")

if _name_ == "_main_":
    main()