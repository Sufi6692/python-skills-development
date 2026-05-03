"""
WHITESPACE CLEANUP IN PYTHON
Methods used:
- strip()   -> removes leading & trailing whitespace
- lstrip()  -> removes leading whitespace
- rstrip()  -> removes trailing whitespace
"""

# -------------------------------
# 1. BASIC WHITESPACE REMOVAL
# -------------------------------

text1 = "   Hello, World!"
print("lstrip():", text1.lstrip())   # "Hello, World!"

text2 = "Hello, World!   "
print("rstrip():", text2.rstrip())   # "Hello, World!"


# -------------------------------
# 2. FULL STRIP OPERATIONS
# -------------------------------

text3 = "   Hello, World!   "

cleaned_text = text3.strip()
print("strip():", cleaned_text)   # "Hello, World!"

leading_cleaned = text3.lstrip()
print("lstrip():", leading_cleaned)   # "Hello, World!   "

trailing_cleaned = text3.rstrip()
print("rstrip():", trailing_cleaned)  # "   Hello, World!"


# -------------------------------
# 3. REMOVING SPECIFIC CHARACTERS
# -------------------------------

text4 = "---Hello, World!---"

# Remove '-' from both sides
cleaned_dash = text4.strip("-")
print("strip('-'):", cleaned_dash)   # "Hello, World!"

# Remove '-' from left
leading_dash = text4.lstrip("-")
print("lstrip('-'):", leading_dash)  # "Hello, World!---"

# Remove '-' from right
trailing_dash = text4.rstrip("-")
print("rstrip('-'):", trailing_dash) # "---Hello, World!"


# -------------------------------
# 4. MIXED WHITESPACE (TABS + NEWLINES)
# -------------------------------

text5 = "\t\n  Hello, World!  \n\t"
print(text5)  # Original text with tabs and newlines

cleaned_whitespace = text5.strip()
print("strip() with tabs/newlines:", cleaned_whitespace)  # "Hello, World!"

text =  "   Hello, World!   "
print(len(text))  # Original length: 25
print(len(text.strip()))  # Length after strip: 13


Nr_of_spaces = len(text) - len(text.strip())
print("Number of spaces removed:", Nr_of_spaces)  # 12
Is_cleaned = len(text) == len(text.strip())
print("Is the text cleaned?", Is_cleaned)  # False