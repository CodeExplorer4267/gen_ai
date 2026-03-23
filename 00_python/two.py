class Car:
    def __init__(self,brand,price,year):
        self.brand=brand
        self.price=price
        self.year=year
        
    def move(self):
        print("The car is moving")
    
    def mileage(self,distance,fuel): #these are methods or actions that the car can perform
        return distance/fuel

car1=Car("Toyota",20000,2020)
print(car1.move())
print(car1.mileage(500,25))
print(car1.brand,car1.price)