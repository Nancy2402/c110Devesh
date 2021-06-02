import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
print(statistics.mean(data))
print(statistics.stdev(data))


fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()

def random_set_of_mean():
    dataset = []
    for i in range(0, 100):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
 meanList=[]
 for i in range(0,1000):
    samplemean=random_set_of_mean()
    meanList.append(samplemean)

 samplingmean=statistics.mean(meanList)
 samplingstdev=statistics.stdev(meanList)
 print(samplingmean)
 print(samplingstdev)  
 df = meanList
 fig = ff.create_distplot([df], ["temp"], show_hist=False)
 fig.add_trace(go.Scatter(x=[samplingmean, samplingmean], y=[0, 1], mode="lines", name="MEAN"))
 fig.show()

setup()  
 


