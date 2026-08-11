#how an generator takes values from another generator 
def gen1():
    yield "Value1"
    yield "Value2"

def gen2():
    yield "Value3"
    yield "Value4"
# def final():
#     yield from gen1()

# ans=final()
# print(next(ans)) #value1
# print(next(ans)) #value2
# print(next(ans)) #error

def final():
    yield from gen1()
    yield from gen2()
# ans=final()
# print(next(ans)) #value1
# print(next(ans)) #value2
# print(next(ans)) #value3

ans=final()
# for item in ans:
#     # print(item)

#how to close a generator . A generator can be stopped before it finishes 
def gen():
    yield "Hello1"
    yield "Hello2"
    yield "Hello3"

ans=gen()
print(next(ans))
print(next(ans))
ans.close()


