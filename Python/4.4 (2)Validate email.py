import re 
email = input("Enter Email: ")
pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")