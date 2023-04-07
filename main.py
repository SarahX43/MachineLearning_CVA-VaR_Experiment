import torch
import pandas as pd

df = pd.read_csv('Stock Prices.csv')
print(df.shape)
print(df.head(10))

df2 = df[df.columns[1:]]
print(df2.shape)
print(df2.head(10))

df3 = df2.iloc[1:]
print(df3.shape)
print(df3.head(10))
