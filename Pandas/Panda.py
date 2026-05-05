import pandas as pd 
s = pd.Series([1, 2, 3, 4, 5])
print("Series:")
print(s)
print("Values:")
print(s.values)
print("Data Type:")
print(s.dtype)
print("Index:")
print(s.index)
print("Name :")
print(s.name)
s.name = "Calories"
print("Updated Name:")
print(s.name)


#Indexing
print("First element:")
print(s[0])
print("Last element:")
print(s[4])

s[0:2] #start(inclusive) and end(exclusive): step value (Value by which the index increases)
print("Slicing:")
print(s[0:2])
print("Slicing with step:")
print(s[0:5:2])

