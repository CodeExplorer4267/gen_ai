# function er moddhe string e chagneg korle original string chnage hoy na
# a="hey"
# def function(str):
#     print(str+"hello")

# function(a)
# print(a)

# if we use list -> it is mutable so function e list change korle original list o change hy
# a=[1,2,3,4]
# def update(list):
#     list.append(94)
#     print("List in the function:",list) #List in the function: [1, 2, 3, 4, 94]
# update(a)
# print("List outside the function:",a) #List outside the function: [1, 2, 3, 4, 94]

# def make(tea,milk,sugar):
#     print(tea,milk,sugar)

# # make("Ginger","yes","Low") #positional
# make(sugar="high",tea="Ginger",milk="Yes") #keywords. here order doesn't matter,

# def special_chai(*ingredients, **extras):
#     print("Ingredients are :",ingredients)
#     print("Extras are",extras)

# special_chai("1","2",a=3,b=48)

# def chai_order(order=[]):
#     order.append('masala')
#     print(order)

# chai_order() #['masala']
# chai_order() #['masala', 'masala']

# #how to fix this -> use None
# def chai_order(order=None):
#     if order is None:
#         order=[]
#         order.append('Masala')
#         print(order)
    
# chai_order()#['masala']
# chai_order()#['masala']