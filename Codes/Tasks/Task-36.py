from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def sound(self):
        pass
    
class Lion(Animal):
    def sound(self):
        print('Roar')
    
class Tiger(Animal):
    def sound(self):
        print('Meoww')
        

lion=Lion()
tiger=Tiger()

print('Lion sounds',lion.sound())
print('Tiger sounds',tiger.sound())