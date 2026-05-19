#create a temp start with 40 increase it with random number at each second until it reaches 100 deg show each step-----------------------------------
# import random 
# import time

# temp=40
# while temp < 100:
#     temp+=random.randint(5,12)
#     print(f"New temp : {temp}")
#     time.sleep(1)

# print(f"Target reached !! current temp : {temp}")

#create a number guessing game with password access ---------------------
import random 
print("------Please sign up first--------")
isGivepass=False
name=input("Please enter your name : ")
password=input("Enter your password:")
isGivepass=True
print("---------Now Login please-----------")
while isGivepass:
    enter_pass=input("Please enter your password")
    if(enter_pass != password):
        print("Your password is wrong!!")
    else:
        isGivepass=False

print(f"---------------Welcome {name} to the number guessing game------------------")
actualNum=random.randint(1,100)
score=0
guessedNum=int(input("Enter a number:"))
while guessedNum != actualNum :
    if guessedNum > actualNum : 
        guessedNum=int(input("Try smaller number"))
    elif guessedNum < actualNum :
        guessedNum=int(input("Try Bigger bigger"))
    else:
        break
    score=score+1

print(f"You found the number !! Your score - {10-score}/10")




