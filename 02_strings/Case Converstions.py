# Case Conversions in Python
text = "Hello, World!"
print("Original Text:", text)
# Convert to uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)  # "HELLO, WORLD!"
# Convert to lowercase
lower_text = text.lower()   
print("Lowercase:", lower_text)  # "hello, world!"
# Convert to title case
title_text = text.title()
print("Title Case:", title_text)  # "Hello, World!"
# Convert to swap case
swap_text = text.swapcase()
print("Swap Case:", swap_text)  # "hELLO, wORLD!"

# -------------------------------
# INPUT (Messy String)
# -------------------------------
raw_text = " 968-Maria, ( Data Engineer ) ;; 27y "


# -------------------------------
# STEP 1: BASIC CLEANUP
# -------------------------------
text = raw_text.strip()  # remove outer spaces

# -------------------------------
# STEP 2: REMOVE ID (968-)
# -------------------------------
text = text.split("-", 1)[1]


# -------------------------------
# STEP 3: EXTRACT NAME
# -------------------------------
name = text.split(",")[0].strip().lower()

# -------------------------------
# STEP 4: EXTRACT ROLE
# -------------------------------
role_part = text.split(",")[1]
role = role_part.replace("(", "").replace(")", "").strip().lower()

# -------------------------------
# STEP 5: EXTRACT AGE
# -------------------------------
age_part = text.split(";;")[1]
age = age_part.replace("y", "").strip()

# -------------------------------
# STEP 6: FINAL OUTPUT
# -------------------------------
result = f"name: {name} | role: {role} | age: {age}"
print(result)
