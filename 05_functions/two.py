#improve function traceability
#add 10% gst to every product you buy and calculate the total price

def calculate_price(order,gst):
    return order*((100+gst)/100)

order_price=[100,568,353,256]
gst_amount=18
total=0
for order in order_price:
    price=calculate_price(order,gst_amount)
    total+=price
    print(f"Original price:{order} -> Final price: {price}")

print("Your total bill is :", total)