#Attribute shadowing -> 
class A:
    name="Rupam"
    roll=12

obj1=A()
print("Original value:",obj1.name) #Rupam
obj1.name="Sam"
print("New value:",obj1.name) #Sam

# del obj1.name
# print("After delete:",obj1.name) #Rupam . it will check if the class have this property. it will print that value

obj1.is_present=True
print("Add a property:",obj1.is_present)

del obj1.is_present
print("After delete",obj1.is_present) #error -> karon class er erom kono propery e nei

