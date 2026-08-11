
file=open("sample.txt","w")
file.write("Koso watashiva soul society")
file.close

file=open("sample.txt","r")
content=file.read()
print(content)

for line in file:
    print(line)
file.close
