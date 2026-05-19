student= {"Name": "Kiran", "Age": 22, "Regno": 562, "Branch": "CSE"}
print("Keys are:")
for x in student:
    print(x)
#print all the values of a dictionary
print("Values are:")
for x in student:
    print(student[x])
#print all the keys and values of a dictionary
print("Keys and values are:")
for x, y in student.items(): #Student items return key value pairs
    print(x,y) #x-key y = value
