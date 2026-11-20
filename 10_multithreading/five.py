#create two threads that will execute a single fucntion.
import threading
import time

def make(type_,waiting_time):
    print(f"{type_} chai started making...")
    time.sleep(waiting_time)
    print(f"Finished {type_}.")

t1=threading.Thread(target=make,args=("Masala",10))
t2=threading.Thread(target=make,args=("Ginger",1))

t1.start()
t2.start()

t1.join()
t2.join()

print("All things done!!!")