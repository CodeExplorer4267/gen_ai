# numbers=[1,2,3,4,5]

# # #general for loop
# # for n in numbers:
# #     print(n)
# #this is comprehension 
# squares=[x**2 for x in numbers]
# print(squares)

# filter the teas which has iced in their name
# menu=[
#     "Masala chai",
#     "Iced lemon tea",
#     "Iced perched tea",
#     "Ginger chai"
# ]
# filtered=[tea for tea in menu if "Iced" in tea]
# print(filtered)
 
num=[1,2,3,4,5,6,7,8,9]
filtered=[n for n in num if n%2 == 0]
# print(filtered)

#set comprehension -> filtering korte kaje lage.
numbers=[1,5,25,6,2,6,7,3,4,2,5,6,7,9,93,53]
uniq_num={num for num in numbers if num > 7}
# print(uniq_num)

#there is a dictinary . in the value part there are duplicates. we have to find the unique value.  
dict={
    "a":[1,5,8,2,4],
    "b":[5,8,2,4,10],
    "c":[11,5,8,3,6]
}

uniq_val={n for numbers in dict.values() for n in numbers}
# print(uniq_val)

