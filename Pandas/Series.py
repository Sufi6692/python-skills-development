import pandas as pd
# Create a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)
print(series.values)
print(series.index)
series.name = "Numbers"
print(series.name)
# Indexing
series[0]
series[0:2] #start(included) : stop (excluded) : step value (values to jump)
series[2:4]

#iloc -> location based indexing
series.iloc[3]
series.iloc[[1,3,4]]


