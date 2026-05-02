# Transformations


stamp = "2024-06-01 12:00:00"
# Split a string into a list of substrings based on a delimiter
date, time = stamp.split(" ")
print("Date:", date)
print("Time:", time)

year,month,day = date.split("-")
print("Year:", year)
print("Month:", month)
print("Day:", day)

csv.file = "1234,Max,USA,1970-10-05,M"
print(csv.file.split(","))
