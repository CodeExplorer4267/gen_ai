# d=dict(one="1",two=2,three=3)
# print(d) #{'one': 1, 'two': 2, 'three': 3}
# #access by key 
# print(d["one"]) 

d={}
d["hello"]=1
d["bello"]=2
d["cjklido"]=3
# print(d) #{'hello': 1, 'bello': 2, 'cjklido': 3}

# #how to delete a key value pair from dictionary
# del d["hello"]
# print(d)

# #membersip test
# print(f"is hello in dict? {'hello' in d}")

# #print the keys , values and items of the dictionary
# print(f"All keys:{d.keys()}")
# print(f"All keys:{d.values()}")
# print(f"All keys:{d.items()}")

#how to get the last item of the dictionary
# last_item=d.popitem()
# print(last_item) #('cjklido', 3)

#create two dic and add them together
# d1={"a":1,"b":2}
# d.update(d1)
# print(d)

#how to get items from dict but without crashing the application if the key is not present
# print(d.get("osohwohvwovhw","NO KEY Present")) #NO KEY Present
# print(d.get("hello","NO KEY Present")) #`1`

#how to loop through a dictionary
for key,value in d.items():
    print(f"Key:{key}->value:{value}")




