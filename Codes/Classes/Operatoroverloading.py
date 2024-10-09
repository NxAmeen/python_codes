class order:
    def __init__(self,a)
        self.cart=cart

    def __len__(self):
        return len(self.cart)

obj=order(['a','b','c','d'])
print('Number of items in cart:',len(obj))



class addition:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a+other.a

obj=addition(10)
obj1=addition(20)

print(obj+obj1)