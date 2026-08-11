#create a logger 
from functools import wraps
import time
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        count=3
        while(count > 0):
            print(f"Preparing your order in {count} seconds")
            time.sleep(1)
            count=count-1
        result=func(*args,**kwargs)
        print("Thank you!! Come again")
        return result
    return wrapper

@my_decorator
def prepare(order,item):
    print(f"Your {order} is prepared with milk status {item}")

# prepare("coffee","With Milk")

#you have a tea inventory. based on your role you get access

def authorization_decorator(func):
    @wraps(func)
    def wrapper(role):
        if role != 'Admin':
            print("You are not admin. Access failed")
            return None
        else:
            return func(role)
    return wrapper
            

@authorization_decorator
def get_inventory(role):
    print("Inventory access granted !!")


new_role=input("Hello!! PLease enter your role:")
get_inventory(new_role)



