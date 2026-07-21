import re
pin = input("Enter PIN Code: ")
pattern = r'^\d{6}$'
if re.match(pattern, pin):
    print("Valid PIN Code")
else:
    print("Invalid PIN Code")