numbers = set()
print(f"Id of the set is: {id(numbers)}")
print(f"Set is {numbers}")
numbers.add(1)
numbers.add(2)

print(f"Id of the set is: {id(numbers)}")   
print(f"Set is {numbers}")

#this is mutable because we can change the set by adding or removing elements, but the id of the set remains the same.
