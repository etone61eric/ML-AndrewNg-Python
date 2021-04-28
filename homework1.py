# Eric Yuan
# Time: 4/28/2021 4:05 PM
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = 'ex1data1.txt'
data= pd.read_csv(path, header=None, names=['population','profit'])
print(data.head())#view the data
print(data.describe())
data.plot(kind='scatter',x='population',y='profit',figsize=(12,8))
plt.show()