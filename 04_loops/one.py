#generate a random token for you and start a system ffrom 0th token . if two matches print it's your turn .

import random 
import time

your_token=random.randint(1,30) #generate a random integer number
temp=your_token
for token in range(1,31):
    print(f"Your turn in {temp} seconds")
    temp=temp-1
    time.sleep(1)
    if token==your_token :
        print("Your turn:")
        break
print("Thank you")

#create a list and print the list names
orders_for=["Rupam1","Rupam2","fjd","fjjf","felekhf"]
for name in orders_for :
    print(name)
    
