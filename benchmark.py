import time
import json
import requests
from fonction import *
import socket


url = "https://mtj-bench.herokuapp.com/benchmarks"
score1=bubbleSortBench()
score2=fileEditBench()
score3=binaryTreeBench()
score4=hanoiBench()
score5=networkBench()
obj = {"hostname": socket.gethostname(), "benchmarks" : [ {"name" : "bubbleSort" , "score" : str(score1)} , {"name" : "fileEdit" , "score" : str(score2)}, {"name" : "binaryTree" , "score" : str(score3)}, {"name" : "hanoi" , "score" : str(score4)}, {"name" : "network" , "score" : str(score5)} ] }
response_json = requests.post(url, data = json.dumps(obj))

print(response_json.text)
