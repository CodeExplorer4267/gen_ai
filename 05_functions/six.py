#pure func-> doesn't change any external var
count=0
def make(cups):
    return cups *10
print(make(10))

#impure func-> uses or changes the external vars
def change():
    global count
    count+=1
    return count
print(change()) #1
print(change()) #2

#lambda func
square=lambda x:x*x
print(square(4))

#create a list and filter 2 from it 
l=[1,2,3,4,2,5,2,6,3,4,2]
ans=list(filter(lambda ele:ele != 2,l))
print(ans)
