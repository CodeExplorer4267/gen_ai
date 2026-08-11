from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(): #we have to create a wrapper function inside it.
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator #this is how we apply the decorators. Er niche ze function seta pass hbe.
def greet():
    print("Hello how are you?")

greet()
#but here the function name changes 
print(greet.__name__) #wrapper

#prevent the function name changing import wraps 




