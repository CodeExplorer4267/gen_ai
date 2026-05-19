# arr=[1,2,3,4,5,6]

# for num in arr:
#     if(num==2):
#         continue
#     if(num==5):
#         print(f"Breaked item : {num}")
#         break
#     print(f"Number is : {num}")

# print("Out of loop")

#for else --------------------
arr=["alice","bob","hendrik"]
searched_name=input("Please enter the name to be searched:")
for name in arr:
    if(name==searched_name):
        print("Found")
        break
else:
    print("Not found")


    