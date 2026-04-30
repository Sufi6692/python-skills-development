## comments
# This is a single-line comment in Python.
"""
    This is a multi-line comment in Python.
    It can span multiple lines and is often used for documentation.
"""
# Store the final exam score in a variable
final_exam_score = 85

final_exam_score = 85 # This variable holds the score of the final exam. 

print("Hi,Python")
print('Hello Python')
#print("Hi")
print("--------------------")
print("    LEARN PYTHON    ")
print("--------------------")

print("Hi \"Python\"") # This will print: Hi "Python"
print('Hi \'Python\'') # This will print: Hi 'Python'
print('Hi "Python"') # This will print: Hi "Python"
print("Hi 'Python'") # This will print: Hi 'Python'
print("C:\\Users\\Username") # This will print: C:\Users\Username
print("Message:\nHello, Python!") # This will print: Message:
print("Message1\n") # This will print: Message1 followed by a new line
print("Message2")

print("Message1\n\n\n") # This will print: Message1 followed by three new lines
print("Message2")
print("Message1\n\n\nMessage2") # This will print: Message1 followed by three new lines and then Message2
print("Message1\tMessage2") # This will print: Message1    Message2 (with a tab space in between)
print("Message1\rMessage2") # This will print: Message2 (Message1 will be overwritten by Message2 due to carriage return)


""" Use PRINT() to recreate this exact output :
    You are allowed to use only one PRINT()
    """
print("\t\t Python Basics \n\t\t Data Engineering \n \t\t Ai ")
# Assigning variables
name = "Khalandar"     # String
age = 22               # Integer
height = 5.8           # Float
is_student = True      # Boolean

# Printing variables
print(name)
print(age)
print(height)
print(is_student)

# Valid
user_name = "Ali"
_age = 25
totalMarks = 90

# Invalid
# 1name = "Error"     # Cannot start with number
# user-name = "Error" # Hyphens not allowed
# class = "Error"     # Reserved keyword

x = 10       # int
x = "Hello"  # now it's string

print(x)

a, b, c = 10, 20, 30
print(a, b, c)

# Same value to multiple variables
x = y = z = 100
print(x, y, z)

num = 50
print(type(num))  # <class 'int'>

x = "100"

# Convert string to integer
y = int(x)

print(y + 50)  # Output: 150

# Student data
student_name = "Khalandar"
marks = 85

# Calculation
result = marks + 5

print(student_name, "scored", result)

