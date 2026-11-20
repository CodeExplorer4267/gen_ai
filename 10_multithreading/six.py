#Image downloading is an IO bound tasks. Why are Threads Better for Downloading Images in Python?

#Case 1 Sequential image download
import requests
import time

image_urls = [
    "https://picsum.photos/id/10/500/500",
    "https://picsum.photos/id/20/500/500",
    "https://picsum.photos/id/30/500/500",
    "https://picsum.photos/id/40/500/500",
    "https://picsum.photos/id/50/500/500"
]

def download_image(url,index):
    response=requests.get(url)
    with open(f"image_{index}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Downloaded {index} file")

start=time.time()
# for i,url in enumerate(image_urls):
#     download_image(url,i)
end=time.time()
# print(f"Total time taken:{end-start:.2f} seconds") #Total time taken:13.62 seconds

#case 2 Multithreading: Download all images concurrently
import requests
import threading
import time

image_urls = [
    "https://picsum.photos/id/10/500/500",
    "https://picsum.photos/id/20/500/500",
    "https://picsum.photos/id/30/500/500",
    "https://picsum.photos/id/40/500/500",
    "https://picsum.photos/id/50/500/500"
]

def download_image(url,index):
    print(f"Downloading {index} image....")
    response=requests.get(url)
    with open(f"Image_{index}.jpg","wb") as file:
        file.write(response.content)
    print(f"Downloaded {index} image!!!")

start=time.time()
threads=[]
for i,url in enumerate(image_urls):
    t=threading.Thread(target=download_image,args=(url,i))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
end=time.time()
print(f"Total time:{end-start:.2f}") #Total time:3.77