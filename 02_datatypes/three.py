a=12
b=20
print(f"Sum is: {a+b}")
print(f"Subtraction is:{a-b}")
print(f"Subtraction is:{b-a}")

print(f"Division is:{a/b}")
print(f"Division is:{b/a}") #it gives the numbers after decimal points 

#only inteter part 
print(f"Integer part : {a//b}") #0
print(f"Integer part : {b//a}") #1

#to get the remainder
print(f"Remainder is: {a%b}") #rem -12 
print(f"Remainder is: {b % a}") #rem - 8

# c=2
c = 100_000_000000_90 # this is valid number in python, we can use underscores to make it more readable
print(f"Power is :{c**4}")