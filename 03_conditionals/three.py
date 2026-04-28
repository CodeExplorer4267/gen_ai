#at first device is offline . after 5 seconds device will be online and asks for temperature after printing the message the device will be offline again

import time
device_status="inactive"
t=5
while t>0:
    t=t-1
    print(f"Device will be active in {t} seconds")
    time.sleep(1)
device_status="active"
print(f"Device is activated!please enter the temperature:")
temp=int(input())
if temp > 35:
    print("Temp alert")
else:
    print("Normal temp")



order_amount=int(input("Enter the order amount:"))
delivery_fees=0 if order_amount > 300 else 30 #ternary operator
print(f"Your total amount:{order_amount+delivery_fees}")