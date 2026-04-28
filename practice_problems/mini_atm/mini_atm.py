user_exit=False
print("Hello welcome to mini atm system.")
user_name=input("Please enter your name:")
print(f"Hello {user_name}!!")
acc_create=False
while user_exit==False:
    print("-----------------------------")
    print("What do you want to do? ")
    print("-----------------------------")
    print("1.create a account")
    print("2.check balance")
    print("3.cash deposit")
    print("4.cash withdraw")
    print("5.exit")
    print("-----------------------------")
    user_input=int(input("Please enter your option:"))

    match user_input:
        case 1:
            if(acc_create==False):
                print("Account created!")
                acc_create=True
                acc_balance=0
            else:
                print("Account already created!")
        case 2:
            if(acc_create==False):
                print("Create a account first")
            else:
               print(f"Account balance is {acc_balance}")
        case 3:
            if(acc_create==False):
               print("Create a account first")
            else:
                deposit_amount=int(input("Enter amount you want to deposit:"))
                acc_balance+=deposit_amount
                print("Your new balance is :",acc_balance)
        case 4:
            if(acc_create==False):
               print("Create a account first")
            else:
                withdraw_amount=int(input("Enter amount you want to withdraw:"))
                if(withdraw_amount > acc_balance):
                    print("You don't have that much amount! Please try again")
                else:
                    acc_balance-=withdraw_amount
                    print("Your account balance is",acc_balance)
        case 5:
            user_exit=True

print("--------Thank you please visit again--------")