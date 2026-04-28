#input seat type from user and pront the features 
seat_type=input("Enter the seat type(sleeper/AC/general/Luxury):").lower()

match seat_type:
    case "sleeper":
        print("It is for sleeping")
    case "ac" | "AC":
        print("It is the AC")
    case "general":
        print("It is the General")
    case "luxury":
        print("It is the Luxury")
    case _:
        print("Invalid seat type") #default type