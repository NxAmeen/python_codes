
class shape:
    def __init__(self,name):
        self.name=name
    
    def area(self):
        pass


class square(shape):
    def __init__(self,side):
        self.side=side
        self.side=int(input("Enter the side:"))
        super().__init__("square")

    def area(self):
        return self.side**2

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        self.radius=int(input("Enter the radius:"))
         super().__init__("circle")

    def area(self):
        return 3.14*self.radius**2

s=square('')
print('Square Details')
print('Area of square:',s.area())

c=circle('')
print('Circle Details')
print('Area of circle:',c.area())