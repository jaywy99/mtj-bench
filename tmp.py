import pandas as pd
from fonction import *

pd.DataFrame({"client_id":[1],"client_hostname" : ["reference"] ,"benchmark": ["bubbleSort"], "Execution time": [bubbleSortBench()], "SPEC_ratio": [1], "Geometric mean": [1]  }).to_csv("records.csv", encoding="utf-8", index=False)
