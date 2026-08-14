class Chai:
    pass

class new_chai:
    pass

chai1=Chai()
# print(type(chai1)) #<class '__main__.Chai'>
# print(type(chai1) is Chai)
# print(type(chai1) is new_chai)

class A:
    name="Rupam"
    section="A"

A.is_present=True #adds a new property

# print(A.is_present)
# print(A.name)
# print(A.section)

obj1=A() #this is object we can access the class properties
obj2=A()
# print(obj1.is_present)

obj1.name="Rupam_new"
# print(A.name) #Rupam
# print(obj1.name) #Rupam_new -> object e property change korle original e change hyna






