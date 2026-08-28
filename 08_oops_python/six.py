#how to access the base class 
class A:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

#but this is code duplication
# class B(A):
#     def __init__(self, name, roll, class_):
#         self.name=name
#         self.roll=roll
#         self.class_=class_

#how to solve it. we explicitly call the base class's constructor(one method)
# class B(A):
#     def __init__(self, name, roll, class_):
#         A.__init__(name,roll)
#         self.class_=class_
        
#Another method for this
class B(A):
    def __init__(self, name, roll,class_):
        super().__init__(name, roll)
        self.class_=class_
