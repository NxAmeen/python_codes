class Car:
    def BMW(self):
        print("This is a luxury car")

class Bike:
    def Gt(self):
        print("This is a cafe racer bike")

class Bus:
    def Volvo(self):
        print("This is a public bus")

class Transport(Car,Bike,Bus):
    def main(self):
        print("This is a my way of transportaion")

obj=Transport()
obj.BMW()
obj.Gt()
obj.Volvo()
obj.main()