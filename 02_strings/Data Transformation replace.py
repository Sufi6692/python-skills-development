print("Data Transformation - replace()")
# Transformation
price = "1234,56"
print(price.replace(",", "."))

phone_number = "123-456-7890"
print(phone_number.replace("-",""))
price = "$1,234.56"
print(price.replace("$", "").replace(",", ""))

#Challenge

""" Convert the messy phone number
 into a clean number format with only digits."""
messy_phone = "+49 (0) 123 456-7890"
clean_phone = messy_phone.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(clean_phone)




