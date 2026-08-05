#dictionary comprehension
#task - create a dictionary from an array 
numbers=[1,2,3,4,5]
dict={n:n**2 for n in numbers}
# print(dict)

#we have a receipe dict where prices are in inr convert it to dollars 
receipes={
    "chai":40,
    "Burger":65,
    "Pizza":100,
}
new_dict={
    item:price/80 for item,price in receipes.items()
}
print(new_dict)