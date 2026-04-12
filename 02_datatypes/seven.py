# tuples=('1','2','3')
# (a,b,c)=tuples
# print(a) #1
# print(b) #2

#assign to indivitual variables 
a,b,c = 2,7,0
print(a,b)
print(c)

#swap the variables 
a,b=b,a
print(a,b)

#to check if a string is in the tuple
my_tuple=("apple","banana","card")
# print(f"Card is present ? {"card" in my_tuple}") -> true
# print(f"Card is present ? {"Card" in my_tuple}") -> False, because of case sensitivity

t1=(1,2)
t2=(3,4)
# print(t1*t2) -> error 
