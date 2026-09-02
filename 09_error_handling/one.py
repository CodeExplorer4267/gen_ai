orders={
    "a":13,
    "b":43
}

#we are trying to access an wrong key
# try:
#     print(orders["C"])
# except KeyError:
#     print("The key does not exist")

# print("Hello")

def serve_chai(flavor):
    try:
        print(f"Preparing your {flavor} chai")
        if flavor=="unknown":
            raise ValueError("We don't serve that chai")
    except ValueError as e:
        print("Error:",e)
    else:
        print("Your chai is served")
    finally:
        print("Next customer please!!")

serve_chai('masala')
serve_chai('unknown')