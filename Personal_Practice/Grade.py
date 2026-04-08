# Program: Calculate average and grade based on subject marks

# Number of subjects
n = int(input("Enter number of subjects: "))

total = 0

# Taking marks input
for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks

# Calculate average
average = total / n

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'

# Output
print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)