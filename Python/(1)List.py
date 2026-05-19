#list operations
numbers =[10,20,30,40]
print("Original Numbers:",numbers)
numbers.append(50)
print("After append:",numbers)
numbers.insert(2,25)
print("After insert:",numbers)
numbers.remove(30)
print("After remove:",numbers)
print("Length of List:",len(numbers))
print("List Elements:")
for item in numbers:
    print(item)