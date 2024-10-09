class operations:

    def add(self, a, b, c=None):
        if a and b is not None:
            print(a + b)
        else:
            print(a + b + c)

obj = operations()
obj.add(1, 2)
obj.add(3, 4, 5)