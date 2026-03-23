from decimal import Decimal
import math
x=2.89
y=-6.56
# print(type(x))
# print(type(y))
print(x+y)
#how to hanlde precision
print(round(x+y,4))
#using decimal module
x=Decimal('2.89')
y=Decimal('-6.56')
print(x+y)

#type conversation
x=89
y=float(x) #then it will print 89.0
print("NEw y is :",y)
#infinity
print(math.inf)