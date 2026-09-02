#how to open a file -> open()
# file=open("order.txt","w")
# try:
#     file.write("My order is burger")
# finally:
#     file.close()

#another method-> it automatically does all the things 
with open("file.txt","w") as file:
    file.write("My order is burger")

#behind the scene the functions call the file.__enter__() , file.__exit__() these dunders