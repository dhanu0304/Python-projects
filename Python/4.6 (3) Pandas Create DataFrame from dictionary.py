import pandas as pd 
students = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(students)
print(df)