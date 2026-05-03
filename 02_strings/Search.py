phone = "+1-800-555-1234"
# Check if the phone number starts with the country code "+1"
print(phone.startswith("+1"))
# Check if the phone number ends with the area code "555"
print(phone.endswith("555"))
# Check if the phone number contains the area code "800"
print("800" in phone)

email = "user@example.com"
print(email.startswith("user"))
print(email.endswith("example.com"))
print("@" in email)

url ="https://www.example.com"
print(url.startswith("https"))
print(url.endswith("com"))
print("example" in url)

#Search
phone1 = "+48-123-456-789"
phone2 = "48-987-654-321"
phone3 = "001-555-123-4567"
print(phone1[3:])
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])