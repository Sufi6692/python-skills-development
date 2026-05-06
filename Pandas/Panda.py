import pandas as pd 
import numpy as np
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

fruit_protein ={
    "Avocado" :2.0,
    "Guava" : 2.6,
    "Blackberries" : 2.0,
    "Oranges" : 0.9,
    "Banana" :1.1,
    "Apples" : 0.3,
    "Kiwi" : 1.1,
    "Pomegranate" : 1.7,
    "Mango" : 0.8,
    "Cherries" : 1.0

 }
print("Fruit Protein Dictionary:")
print(fruit_protein)
s2 = pd.Series(fruit_protein, name="Protein")
print(s2)

# Conditional Selection
print("Fruits with protein content greater than 1 gram:")
print(s2[s2 > 1])
# Logical Operators
print("Fruits with protein content between 0.5 and 2 grams:")
print(s2[(s2 >0.5) & (s2 < 2)])
# or operator
print("Fruits with protein content less than 0.5 or greater than 1.5 grams:")
print([(s2 < 0.5) | (s2 > 1.5)])
# Not operator
print("Fruits with protein content not greater than 1 gram:")
print(~(s2 > 1))
# Modyfing the series
s2["Mango"] = 2.8
print("Updated Series:")
print(s2)

ser = pd.Series(['a',np.nan, 1,np.nan, 2])
print("Series with NaN values:")
print(ser)
print("Checking for NaN values:")
print(ser.isnull())
print("Checking for non-NaN values:")
print(ser.notnull())
print(s.notnull().sum()) #count of non-NaN values

#DataFrame :
data = {
    "Name" : ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age" : [25, 30, 35, 40, 45],
    "salary" : [50000, 60000, 70000, 80000, 90000],
    "Department" : ["HR", "Finance", "IT", "Marketing", "Sales"],
    "City" : ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("DataFrame Info:")
print(df.info())
df.head(2) #first 2 rows
df.tail(2) #last 2 rows

# loc and iloc
print("Using loc:")
print(df.loc[0]) #first row
print("Using iloc:")
print(df.iloc[0]) #first row
print(df.iloc[1:3,:2]) #rows 1 and 2, columns 0 and 1
print("Using loc with column names:")
print(df.loc[1:3, "Name":"Age"]) #rows 1 to 3, columns "Name" to "Age"
print("Using loc with specific columns:")
print(df.loc[1:3, ["Name", "Age"]]) #rows 1 to 3, specific columns "Name" and "Age"

df[["Age", "City"]] #selecting specific columns
print("Selecting specific columns:")
print(df[["Age", "City"]])
print("Conditional Selection:") 
print(df[df["Age"] > 30]) #rows where age is greater than 30
print("Multiple Conditions:")
print(df[(df["Age"] > 30) & (df["Department"] == "IT")]) #rows where age is greater than 30 and department is IT
# drop
print("Dropping a column:")
print(df.drop("Age", axis =1 )) #drop the "Age" column

# checking the issue 

