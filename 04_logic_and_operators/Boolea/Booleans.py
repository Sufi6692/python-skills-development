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








