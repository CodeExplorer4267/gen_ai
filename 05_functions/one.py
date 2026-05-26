#receive each customers name and order and print them

# def print_order(name,order):
#     print(f"{name} ordered {order}!!")

# print_order("Rupam","Momo")
# print_order("Rupam2","Biriyani")

#take the name,email and password from user-> validate the user info -> save to the database -> after registering move user to the login page -> do the login -> then complete
import re

def validate_input(name,email,password):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if(not re.match(pattern,email)):
        print("Enter valid email type:")
        return False
    if(len(password) < 8):
        print("Enter password greater than 8 chatracters")
        return False
    print("Validation done !!")
    return True

def save_to_db(name,email,password):
    print("Successfully saved to database")

name=input("Enter your name:")
email=input("Enter your email:")
password=input("Enter password : ")

def register_user(name,email,password):
    is_validate=validate_input(name,email,password)
    if(is_validate):
        save_to_db(name,email,password)
    else:
        print("Validation Failed!!")


register_user(name,email,password)