import re
phone = input("Enter your mobile number: ")
pattern = r'^[6-9]\d{9}$'
if re.match(pattern, phone):
    print("Valid mobile number")
else:
    print("Invalid mobile number")