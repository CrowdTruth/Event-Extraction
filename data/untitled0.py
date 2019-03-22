import hashlib
import pandas as pd


dataset = pd.read_csv('pilot_crowd_data/raw_data/f1323748_timeexpressions_allmotivation.csv')

for i in range(len(dataset.index)):
    m = hashlib.md5()
    m.update(str(dataset["_worker_id"].iloc[i]).encode())
    dataset["_worker_id"].iloc[i] =  m.hexdigest()

    m = hashlib.md5()
    m.update(str(dataset["_ip"].iloc[i]).encode())
    dataset["_ip"].iloc[i] =  m.hexdigest()
   
dataset.to_csv('pilot_crowd_data/raw_data/f1323748_timeexpressions_allmotivation.csv', index=False)