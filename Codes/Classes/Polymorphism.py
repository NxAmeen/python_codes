class square():
    def __init__(self,side):
        self.side=side
        self.side=int(input("Enter the side:"))

    def area(self):
        return self.side**2

class circle():
    def __init__(self,radius):
        self.radius=radius
        self.radius=int(input("Enter the radius:"))

    def area(self):
        return 3.14*self.radius**2

s=square('')
print('Square Details')
print('Area of square:',s.area())

c=circle('')
print('Circle Details')
print('Area of circle:',c.area())