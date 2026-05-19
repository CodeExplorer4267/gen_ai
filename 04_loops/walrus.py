# value=13
# remainder=value % 5

# if remainder:
#     print(f"Not divisible, the remainder is :{remainder}")

# value=13

# if(remainder:=value%5):
#     print(f"Not divisible, the remainder is :{remainder}") ----1

# line=input("Enter your text")
# while(line != "quit"):
#     print("You typed:", line)
#     line = input("Enter text: ")
# print("Over")

# --convert it to walrus

# while (line := input("Enter text: ")) != "quit":
#     print("You typed:", line)
# ---------2

#check if cupsize is available or not 
# available_size=["small","medium","large"]

# if(requested_size := input("Enter your size:")) in available_size:
#     print(f"Serving the cupsize : {requested_size}")
# else:
#     print(f"Sorry cup size is not available")-----------------3

# ---------------------------------

#show what are the available foods are there -> user choose the product and quantity -> calculate total -> user can see what are the available coupens are there -> they can claim it and got discount -> show the discounted price 

print("-----------Our menu-------------")
print("1.Burger - 10$  2. Pizza - 15$  3.Momo - 7$")
print("4.Chickenthali - 16$  5. Vegthali - 10$  6.SeaFood - 12$")
print("--------------------------------")

coupen_num_with_random_num={
    "1":"FA2",
    "2":"HF4",
    "3":"O97",
    "4":"Y73",
    "5":"PK8"
}

discounts={
    "FA2":(0.2,0),
    "HF4":(0.3,0),
    "O97":(0,12),
    "Y73":(0.18,0),
    "PK8":(0,20),
}

def calculate(item,quantity):
    match item:
        case "burger":
            return quantity*10
        case "pizza":
            return quantity*15
        case "momo":
            return quantity*7
        case "chickenthali":
            return quantity*16
        case "vegthali":
            return quantity*10
        case "seafood":
            return quantity*12
        case _:
            print("Invalid item")
            return 0
 
user_orders=[]
user_order_done=False
while user_order_done==False:
    item=input("Please Enter your order:").lower()
    quantity=int(input("How many do you want?"))
    user_orders.append([item,quantity])
    if(user_query:=input("Do you want to finish ordering?").lower()) == 'yes':
        user_order_done=True

total=0
for item,quantity in user_orders:
    total=total+calculate(item,quantity)

print("Your total bill is:",total)

coupen_num=input("You have coupens to spend!! Please enter a number between 1 to 5")
print("You have got the coupen : ", coupen_num_with_random_num[coupen_num])
coupen= coupen_num_with_random_num[coupen_num]
dis_percen,dis_amou=discounts[coupen]
if not dis_amou:
    total=total-(total*(dis_percen*100)/100)
else:
    total=total-dis_amou

print("Your discounted price:",total)


