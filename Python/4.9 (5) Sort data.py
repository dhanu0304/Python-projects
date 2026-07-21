import pandas as pd 
data={"Name": ["Amit", "Rahul", "Priya"],
      "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
print(df.sort_values(by="Marks"))
