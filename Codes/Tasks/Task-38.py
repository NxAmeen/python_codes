class alphabets:
    def __init__(self):
        self.current=65
        self.end=90

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>self.end:
            raise StopIteration
        letter=chr(self.current)
        self.current+=1
        return letter
    
alpha=alphabets()
for letter in alpha:
    print(letter)

