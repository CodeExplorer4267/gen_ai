#create a program where user will say the order you have to calculate the bill

def calculate(cup_size,number_of_cups):
    if(cup_size=="small"):
        return 10*number_of_cups
    elif(cup_size=="medium"):
        return 15*number_of_cups
    elif(cup_size=="large"):
        return 20*number_of_cups
order_end=False
total_bill=0
while not order_end:
    cup_size=input("What size of cup do you want? (small/medium/large)").lower()
    number_of_cups=int(input("How many cups do you want"))
    total_bill=total_bill+calculate(cup_size,number_of_cups)
    end=input("Do you want to end your order?").lower()
    if(end=="yes"):
        order_end=True
        break
    else:
        continue
print(f"Your total bill is:{total_bill}")