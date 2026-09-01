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

class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size

    #suppose we are accepting data from dictionary
    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    #suppose we are accepting data from string
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split(',')
        return cls(tea_type,sweetness,size)

order1=ChaiOrder.from_dict({
    "tea_type":"masala",
    "sweetness":"medium",
    "size":"Large"
})

order2=ChaiOrder.from_string("Ginger,low,small")
# print(order1) #<__main__.ChaiOrder object at 0x0000027D0E456BA0>
print(order1.__dict__) #{'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}


