class power_operation:
    def __init__(self,maximum=0):
        self.maximum=maximum
    
    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n<=self.maximum:
            result=self.n**2
            self.n+=1
            return result
        else:
            raise StopIteration
    
    
number=power_operation(5)
i=iter(number)
print(next(i))
print(next(i))
print(next(i))
