#multiprocessing. We have many servers. different dish banabe.
from multiprocessing import Process
import time

def make(name):
    print(f"start preparing of ${name} dish")
    time.sleep(3)
    print(f"Prepare done!!")

if __name__ == "__main__":
    makers=[
        Process(target=make,args=(f"Maker:${i}",))
        for i in range(1,4)
    ]

#start the processes 
    for p in makers:
        p.start()
#wait for all to complete
    for p in makers:
        p.join()
    print("All dishes are served!!")
