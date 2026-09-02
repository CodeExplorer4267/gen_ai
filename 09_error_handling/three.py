#creating custom exceptions
#there is an exception class we have to perform inheritance 
class OutofIngredientsError(Exception):
    pass

def process_chai(milk,sugar):
    if milk == 0 or sugar==0:
        raise OutofIngredientsError("Not enough")
    print("chai is ready")

process_chai(0,1)