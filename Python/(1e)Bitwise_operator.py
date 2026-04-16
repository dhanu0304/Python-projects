x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
a1=x&y #bitwise AND
a2=x|y #bitwise OR
a3=~x #bitwise NOT
a4=x^y #bitwise XOR 
a5=x>>2 #right shift
a6=x<<2 #left shift
print("Bitwise AND:",a1)
print("Bitwise OR:",a2)
print("Bitwise NOT:",a3)
print("Bitwise XOR:",a4)
print("Right shift:",a5)
print("Left shift:",a6)
