a=int(input("Enter 1 no:"))
b=int(input("Enter 2 no:"))
print("1.ADD")
print("2.Sub")
print("3.Div")
print("4.Multi")

choice = int(input("Enter your choice:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a/b)
elif choice==4:
    print(a*b)
else:
    print("Invalid choice")