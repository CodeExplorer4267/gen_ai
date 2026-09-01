orders={
    "a":13,
    "b":43
}

#we are trying to access an wrong key
try:
    print(orders["C"])
except KeyError:
    print("The key does not exist")

print("Hello")