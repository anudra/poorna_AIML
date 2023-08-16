import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-04/Desktop/dataset/iris.csv")
print(data)
print(data.head(5))
print(data.tail(12))
print(data["PetalWidthCm"])
print(data.count())
print(data.info())
print(data.dtypes)
