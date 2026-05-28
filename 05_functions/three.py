
# def serve_chai():
#     chai_type="Masala" #local
#     print(f"Serving chai type : {chai_type}")


# chai_type="Lemon"
# serve_chai()
# print(f"Serving {chai_type}")

# def update():
#     a=12
#     def update2():
#         a=23
#     update2()
#     print("Value is:",a) #12 -> because it is refering the local one 

# update()

# def update():
#     a=12
#     def update2():
#         nonlocal a
#         a=134
#     update2()
#     print("Value is:",a) #134 -> now it can access the inside 

# update()

# a="hello"
# def func1():
#     def func2():
#         # global a #it can access the global a 
#         nonlocal a #No binding for nonlocal "a" foundPylance 
#         a="hey"
    
#     func2()
# func1()
# print(a)
