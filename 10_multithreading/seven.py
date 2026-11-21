#Threading Lock :
import threading
import time

balance = 1000

lock=threading.Lock() #add a threading lock

def withdraw(amount):
    global balance
    with lock:
        temp = balance
        time.sleep(0.1)

        balance = temp - amount

t1 = threading.Thread(target=withdraw, args=(500,))
t2 = threading.Thread(target=withdraw, args=(300,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance) #700 this is wrong. After lock it will show the correct amount : 200