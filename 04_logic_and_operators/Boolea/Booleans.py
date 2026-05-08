# Booleans

# Values - True and False
print(True)
print(False)
print(type(True))
print(type(False))

# Functions bool() 
print(bool(1234))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# any()

email = "sufikhalandar@gmail.com"
phone = "026548-6465"
username = "sufi669200"

#Allow registration
# if any field is filled
print(any([email,phone,username]))

# all ()

#Allow registration
#only of all fields is filled

print(all([email,phone,username]))

# isinstance ()
print(isinstance(123,int))
print(isinstance(True,str))


print("Hello".endswith("o"))
print("Hello".startswith("o"))



# Comparison Operators

print(10 == 10 )
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print(7 <= 7)


# String Can be compared too!
# You can compare strings too alphabetically, not just numbers

print("a" < "b")
print("a" ==  "b")


# Python is case-sensitive
# So "a" and "A" are treated as different values
print("a" ==  "A")


#Chained Comparison
# It evaluates if from left to right, checking each condition one by one

print(1 < 4 < 6) # True
print(5 < 4 < 6) # False



#Chained Comparison
# Work like SQL's BETWEEN They check if a value is between two bounds

# Is age between 18 and 30 ?
age = 18
print(18 <= age <= 30)



