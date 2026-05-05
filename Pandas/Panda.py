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

#iloc --> Location based indexing
print("Using iloc:")
print(s.iloc[0]) #first element
print(s.iloc[4]) #last element
print("Slicing with iloc:")
print(s.iloc[0:2]) #first two elements
print("Slicing with iloc and step:")
print(s.iloc[0:5:2]) #first five elements with step of 2
index = ["apple", "banana","grapes", "orange", "mango"]
s.index = index
print("Updated Index:")
print(s.index)
print(s)
print("Accessing element with new index:")
print(s["apple"])
print("Slicing with new index:")
print(s["apple":"grapes"]) #start(inclusive) and end(inclusive)
# In label based indexing your start as well as stop value both are included in the output.
s["apple":"grapes":2] #start(inclusive) and end(inclusive): step value (Value by which the index increases)
print("Slicing with new index and step:")
print(s["apple":"grapes":2])

