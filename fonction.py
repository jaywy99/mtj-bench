import time
import os
import random
import requests

def bubbleSortBench(): 
    starting = time.time()
    print("Benchmark 1 is computing, please wait...")
    arr = [i for i in range(10000,0, -2 )]
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
    end = time.time()
    print("Done Benchmark 1 ")
    return end-starting


def fileEditBench():
    start = time.time()
    print("Benchmark 2 is computing, please wait...")
    for i in range(1000):
        with open("tmp.txt","a") as f:
            f.write("f"*1000000)
    end = time.time()
    os.remove("tmp.txt")
    print("Done Benchmark 2 ")
    return end-start
    
def binaryTreeBench():
    start = time.time()
    print("Benchmark 3 is computing, please wait...")
    class Node:

        def __init__(self, data):

            self.left = None
            self.right = None
            self.data = data

        def insert(self, data):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

    root = Node(12)
    for i in range(1000000):
        root.insert(random.randint(-1000000,1000000))
    
    end = time.time()
    print("Done Benchmark 3 ")
    return end-start
    
    
def hanoiBench():
    def hanoi(n,dep,inter,dest):
      if n==1:
        pass
        #print(dep,"----->",dest)
      else:
        hanoi(n-1,dep,dest,inter)
        #print(dep,'----->',dest)
        hanoi(n-1,inter,dep,dest)
    start=time.time()
    print("Benchmark 4 is computing, please wait...")
    hanoi(28,"A","B","C")
    end=time.time()
    print("Done Benchmark 4 ")
    return end-start


def networkBench():
    start=time.time()
    print("Benchmark 5 is computing, please wait...")
    url="http://www.teleliban.com.lb"
    request = requests.get(url)
    end=time.time()
    print("Done Benchmark 5 ")
    return end-start
