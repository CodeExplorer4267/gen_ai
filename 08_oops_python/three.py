class A:
    size=139
    def print_size(self):
        return print("The size is:",self.size)

obj1=A() 
# print(obj1.print_size()) #it passes the object's reference
obj2=A()
obj2.size=482
# print(obj2.print_size())

# print(A.print_size()) #it does not know which object -> error
#sol
print(A.print_size(obj1)) #139
print(A.print_size(obj2)) #482

