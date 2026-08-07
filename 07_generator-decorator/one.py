def generator():
    yield "Hello 1"
    yield "hello2"
    yield "hello3"

ans=generator()

# for a in ans:
    # print(a)

#difference between function and generator 
def get_list():
    return ["Cup1","Cup2","Cup3"]

def gen_list():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"

ans=gen_list()
# print(ans) #output will be an generator object so it is just a referecne 
# so how to print the values 
# print(next(ans)) #cup1 and the function will be pause executing 
# print(next(ans)) #cup2 -> zekhan thek pause hyechilo sekhan thek start hbe.

#infinite generators
def infinite_gen():
    count=1
    while True:
        yield f"Refill no. {count}"
        count+=1
user1=infinite_gen()
user2=infinite_gen()

for _ in range(4):
    print(next(user1))

for _ in range(5):
    print(next(user2))

#duto user er jonno alada refill track korte pari. mix kore dey na 