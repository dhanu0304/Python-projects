import re
text ="Roll numbers are 101,102,103 and 104."
numbers = re.findall(r'\d+', text)
print(numbers)