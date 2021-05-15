import pandas as pd

data = pd.read_csv("satisfaction.csv")

def Sort():
   
    print(data.head(5))

def valueSort():

    print(data.iloc[0])

print(valueSort())
