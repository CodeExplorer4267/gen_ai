#create a billing system where user will order and calculate the total bill. handle all the errors gracefully

class OutofIngredientsError(Exception):
    pass

def calculate(item,quantity,menu):
    cost=0
    try:
        if item not in menu:
            raise OutofIngredientsError("Item is not available")
        if not isinstance(quantity,int):
            raise TypeError("Please enter integer quantity")
        cost=menu[item]*quantity
    except Exception as e:
        print("Error:",e)
    else:
        print("Item added")
    finally:
        return cost


print("\n==============================")
print("        🍽️ FOOD MENU")
print("==============================")
print("1. 🍕 Pizza       - ₹250")
print("2. 🍔 Burger      - ₹150")
print("3. 🍝 Pasta       - ₹200")
print("4. 🍟 French Fries - ₹100")
print("5. 🥤 Cold Drink  - ₹80")
print("6. Exit")
print("==============================")
print("Please enter your order!!")
orders=[]
order_done=False
menu={
    "pizza":250,
    "burger":150,
    "pasta":200,
    "fries":100,
    "colddrink":80
}
total_bill=0
while not order_done:
    item=input()
    quan=int(input("Enter the quantity"))
    total_bill=total_bill+calculate(item,quan,menu)
    finish=input("DO you want anything more?")
    if(finish=="no"):
        order_done=True
    else:
        order_done=False
print(f"Your total bill : {total_bill}")
    


