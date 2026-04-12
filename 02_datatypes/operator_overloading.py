# print(2+3)
# print("Hello "+"World")

# a=[1,2,3]*3
# print(a) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

# class Point:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self, other):
#         return Point(self.x+other.x,self.y+other.y,self.z+other.z)
#     def __sub__(self, other):
#         return Point(self.x-other.x,self.y-other.y,self.z-other.z)
#     def __mul__(self, other):
#         return Point(self.x*other.x,self.y*other.y,self.z*other.z)-Point(self.x-other.x,self.y-other.y,self.z-other.z)
#     def __str__(self):
#         return f"({self.x},{self.y},{self.z})"
    
# p1=Point(1,2,3)
# p2=Point(4,5,6)
# # result=p1+p2
# # result=p1-p2
# result=p1*p2 #(4,10,18)-(-3,-3,-3)=(7,13,21)
# print(result)

#bytearray :

# b=bytearray("Hello World","utf-8")
# # print(b) #bytearray(b'Hello World')
# # print(b[0]) #72 -> kono char er ascii value return kore
# # print(b[1]) #101

# b=bytearray([65,66,67,68])
# b[0]=102 #mutable
# print(b) #bytearray(b'ABCD')

# b=bytearray(5)
# print(b) #bytearray(b'\x00\x00\x00\x00\x00')

