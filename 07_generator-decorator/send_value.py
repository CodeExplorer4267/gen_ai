import time
def prepare():
    print("Welcome!! Please give your order.")
    order=yield #in this line it is waiting for an order
    while True:
        print(f"Preparing your {order}...")
        order=yield

stall=prepare()
next(stall) #line no. 2 obdhi asbe then waiting for order

stall.send("Burger")

#create a system where it takes order from customers....it waits 10 seconds if user forget something ..if user doesn't order ....it confirms your order (***check the code)

print("Welcome to our shop!!")
time.sleep(3)
print("Please place your order!!")
print("1.Burger(65) 2.Pizza(100) 3.Momos(50) 4.Noodles(100) 5.Chicken Roll(65)")
dictionary={
    "Burger":65,
    "Pizza":100,
    "Momos":50,
    "Noodles":100,
    "Roll":65
}
order_done=False
orders=[]
cost=0
while not order_done:
    item=input("Please write your order.")
    orders.append(item)
    cost += dictionary[item]
    string=input("do you want to finish your order?").lower()
    if string=="yes" or string=="ok":
        order_done=True

def prepare():
    global cost

    print("Please give your extra order:")
    order = yield

    while True:
        print(f"Adding {order}")
        orders.append(order)
        cost += dictionary[order]
        order = yield

new_add = prepare()
next(new_add)          # Start generator

while True:
    extra = input("Anything left? ").lower()

    if extra == "yes":
        item = input("Enter item: ")
        new_add.send(item)
    else:
        break

print("Orders:", orders)
print("Final Bill:", cost)

    




    




