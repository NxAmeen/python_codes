from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        print("This is method2")

class demo1(demo):

    def method1(self):
        print("This is a method")

    def method3(self):
        print("This is method3")




obj1=demo1()
obj1.method1()
obj1.method3()





# from abc import ABC, abstractmethod

# class tv(ABC):
#     @abstractmethod
#     def show_channel(self):
#         pass

    
# class smarttv(tv):
#     def show_channel(self):
#         print("This is smart TV")

  

# class ledtv(tv):
#     def show_channel(self):
#         print("This is LED TV")


# def channel(tv) :
#     tv.show_channel()




# smarttv=smarttv()
# ledtv=ledtv()

# channel(smarttv)
# channel(ledtv)