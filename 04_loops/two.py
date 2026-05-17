#create a menu board and list all the items with a number start from 1
# menu=["one","two","three"]

# for index,m in enumerate(menu,start=1):
#     print(f"{index}. {m}")

#input your name -> menu will be shown to you -> (item,price) -> order(item,queantity)-> 

def calculate(order,quantity):
    match order:
        case "burger":
            return quantity*65
        case "pizza":
            return quantity*100
        case "momo":
            return quantity*45
        case "fuchka":
            return quantity*30

items=["Burger:65","Pizza:100","Momo:45","Fuchka:30"]

name=input("Enter your name:")

print("----Please order from this menu----")
for index,item in enumerate(items):
    print(f"{index}. {item}")
print("-----------------------------------")
user_order_done=False
total_bill=0
while not user_order_done:
    order=input("Please enter your item:").lower()
    quantity=int(input("How many do you want?"))
    total_bill+=calculate(order,quantity)
    order_done=input("Do you want to finish your order?").lower()
    if order_done=="yes":
        user_order_done=True
    else:
        continue
print("Your total bill is :",total_bill)
payment=int(input("Please pay the bill:"))
if(payment==total_bill):
    print("Thank you!!")


