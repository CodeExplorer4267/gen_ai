class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal): #inheritance
    def barking(self):
        print("Dog is barking")

d=Dog()
# print(d.barking())
# print(d.eat())

# class new:
#     chai_cls=Animal #we can hold any of the class in a variable.
#     def __init__(self):
#         self.chai=self.chai_cls()
#         print(self.chai)

#composition= creating a class by containing an object of another class
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine=Engine()

    def start_car(self):
        self.engine.start()

car=Car()
car.start_car()
