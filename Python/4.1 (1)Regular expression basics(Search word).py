import re
text ="Python is a powerful programming language."
pattern="powerful"
result=re.search(pattern,text)
if result:
    print("Pattern found")
else:
    print("Pattern not found")