# static method
class A:
    def getItems(self,a,b):
        return a+b

#inorder to access the method we have to create object
a=A()
# print(a.getItems(4,7))
#but object create na kore class name diyeo access korte pari

class A:
    @staticmethod
    def add(a,b):
        return a+b

# print(A.add(5,69))

#classmethod vs static method



