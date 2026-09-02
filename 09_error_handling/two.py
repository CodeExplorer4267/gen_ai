#how to handle multiple exceptions
def process_order(item,quantity):
    try:
        price={"burger":60,"pizza":100}[item] #this is just value extraction from dictionary
        
        if quantity > 0:
            cost=price*quantity
        else:
            raise TypeError("Please enter a valid quantity")
            
    except KeyError:
        print(f"That item is not available in the menu")
    except TypeError:
        print(f"Please enter a valid quantity")
    else:
        print(f"Your total bill is : {cost}")
    finally:
        print("Next customer!!")
# process_order("pizza",3) #300
# process_order("rice","two") #That item is not available in the menu
# process_order("burger","two") #Please enter a valid quantity



