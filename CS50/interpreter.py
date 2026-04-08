expression=input("Enter your expression: ").strip()
x,y,z = expression.split()
x= float(x)
z= float(z)
if y== "+":
    result = x+z
    print(result)
elif y== "-" :
    result = x-z
    print(result)
elif y== "*":
    result = x*z
    print(result)
elif y== "/":
    result = x/z
    print(result)
else :
    print('error')