class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth


class rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)    


class square(shape):
    def __init__(self,side):
        super().__init__(side,side)


r=rectangle(10,20)
s=square(10)
print('Area of rectangle:',r.area())
print('Area of square:',s.area())