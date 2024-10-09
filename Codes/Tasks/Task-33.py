from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculateArea(self):
        return 3.14*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calculateArea(self):
        return self.length*self.breadth
    
radius=float(input('Enter the radius of the circle: '))
Circle=Circle(radius)
print(f'Area of the circle: {Circle.calculateArea()}')

length=float(input('Enter the length of the rectangle: '))
breadth=float(input('Enter the breadth of the rectangle: '))
Rectangle=Rectangle(length,breadth)
print(f'Area of the rectangle: {Rectangle.calculateArea()}')