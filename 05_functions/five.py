def make():
    # return "Hello this is return"
    print("hello this is return")

#1.  print(make()) #direct print the return value
#2.  return_value=make()
# print(return_value) #we store the returned value and then print

return_value=make()
print(return_value) #None-> function does not return anything

#case -> return one value
def make():
    return 120

store=make()
print(store)

# #case-> early return
def make(cup):
    if cup==0:
        return "Sorry we don't have cups"
    return "order ready"
    
print(make(0))
print(make(3))

#case -> return multiple value
def make():
    return 10,20,30
# a,b=make() #zoto gulo returned value toto gulo var e store korte hobe. else -> error 
a,b, _=make() #we can ignore the extra var without getting error.
print(a)
print(b)

