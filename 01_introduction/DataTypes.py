#Data Types
a = 10 # a is an integer
b = 3.14 # b is a float
c = "Hello" # c is a string
d = 'A' # d is a character (string of length 1)
e = "1234" # e is a string, not an integer
f = True # f is a boolean
g = False # g is a boolean
h = None # h is a special value representing "no value"
i = "" # i is a str blank string
j = " " # j is a string containing an empty space
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'str'>
print(type(f)) # <class 'bool'>
print(type(g)) # <class 'bool'>
print(type(h)) # <class 'NoneType'>
print(type(i)) # <class 'str'>
print(type(j)) # <class 'str'>


# Functions + Data Types
text  = "Hello, World!"
number = 42
 
print(text)
print(number)

print(type(text)) # <class 'str'>
print(type(number)) # <class 'int'>

print(len(text)) # 13
# print(len(number)) # TypeError: object of type 'int' has no len()


print(text.upper()) # "HELLO, WORLD!"
print(number.bit_length()) # 6 (number of bits needed to represent 42 in binary

# Python Challenge 
# Create 5 variables -each of a different data type
""" 
1.Your age
2.Your height
3.Your name
4.Are you a student?
5.Something that has no value yet
"""
# Then print the values, data types, lengths of all variables

age = 21
height = 5.5
name = "Sufian"
Is_student = True
no_value = None
print(age, type(age), age.bit_length()) # 21 <class 'int'> 5
print(height, type(height),) # <class 'float'> 4
print(name, type(name), len(name)) # Sufian <class 'str'> 6
print(Is_student, type(Is_student)) # True <class 'bool'>
print(no_value, type(no_value)) # None <class 'NoneType'>

