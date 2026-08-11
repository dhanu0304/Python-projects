a=int(input("Enter first number:"))
b=int(input("enter second number:"))

#relational:
print(a<b)
print(a>b)
print(a==b)
print(a!=b)

#Logical: AND , OR < Not
print(a>b and b>=10)
print(a>b or b>=10)
print(not a>b)

print("Bitwise")
print("NOT=",a>b & a<10)
print("OR=", a<10 | b>100)
print("Not=",~a<10)