import pandas as pd
data= {"Marks": [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

print("Average=", df["Marks"].mean())
print("Sum=", df["Marks"].sum())
print("Maximum=", df["Marks"].max())
print("Minimum=", df["Marks"].min())