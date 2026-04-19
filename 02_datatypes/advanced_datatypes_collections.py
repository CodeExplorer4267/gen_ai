# import arrow 

# time=arrow.utcnow()
# print(time)

#count frequency of characters in a array + strings
# from collections import Counter

# a=["a","b","c","a","b","a"]
# counter=Counter(a)
# print(counter) #Counter({'a': 3, 'b': 2, 'c': 1})
# print(counter["a"]) #3

#create a default dict
# from collections import defaultdict
# d=defaultdict(int)
# d["hello"]+=1
# print(d)
# print(d["hehfhwgvkh"]) #0 there will be no error even if the key is not present because of the default value of int which is 0

# from collections import namedtuple

# Student = namedtuple("Student", ["name", "age"])

# s = Student("Ruma", 21)
# print(s.name)  # Ruma

# from collections import deque
# d=deque()
# d.append(1) #append to the right
# d.append(2)
# d.append(3)
# print(d)
# d.appendleft(5)
# print(d)
# print(d.count(2))
# d.clear()
# print(d)