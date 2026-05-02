#Indexes & Slicing
text = "Python"

#Extracting the first character
print(text[0])
#Extracting the last character
print(text[-1])
#Extracting a substring
print(text[1:4]) #Extracts characters from index 1 to 3 (
#Extracting a substring with a step
print(text[0:6:2]) #Extracts characters from index 0 to
#5 with a step of 2 (Pto)
#Extracting a substring from the beginning to a specific index
print(text[:4]) #Extracts characters from the beginning to index 3 (Pyth)
#Extracting a substring from a specific index to the end
print(text[2:]) #Extracts characters from index 2 to the end (thon)
#Extracting a substring with negative indexing
print(text[-4:-1]) #Extracts characters from index -4 to -2 (tho)   

date = "2024-06-01"
#Extracting the year
year = date[0:4]
date [:4] #Extracts the year (2024)
#Extracting the month
month = date[5:7]
date [5:7] #Extracts the month (06)
#Extracting the day
day = date[8:10]
date [8:10] #Extracts the day (01)  
date [-2:]
date [8:] #Extracts the day (01) using negative indexing

print(year)
print(month)
print(day)