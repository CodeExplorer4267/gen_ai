#mro
class A:
    label="This is class A"

class B(A):
    label="This is class B"

class C(A):
    label="This is class C"

# class D(B,C):
#     pass
class D(C,B):
    pass

d=D()
# print(d.label) #This is class B
# print(d.label) #This is class C -> line 13
print(D.__mro__) #(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
