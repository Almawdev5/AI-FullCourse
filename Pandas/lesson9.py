# Lesson 9: Filtering Data

import pandas as pd

# -----------------------------
# Create DataFrame
# -----------------------------
data = {
    "Name": ["Alex", "Sara", "John", "Mike"],
    "Age": [22, 21, 23, 24],
    "Score": [95, 88, 76, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# -----------------------------
# One condition
# -----------------------------
print("\nScore > 80")
print(df[df["Score"] > 80])

# -----------------------------
# Age >= 23
# -----------------------------
print("\nAge >= 23")
print(df[df["Age"] >= 23])

# -----------------------------
# AND condition
# -----------------------------
print("\nAge > 21 AND Score > 80")
print(df[(df["Age"] > 21) & (df["Score"] > 80)])

# -----------------------------
# OR condition
# -----------------------------
print("\nScore > 90 OR Age < 22")
print(df[(df["Score"] > 90) | (df["Age"] < 22)])

# -----------------------------
# Filter by name
# -----------------------------
print("\nStudent named Sara")
print(df[df["Name"] == "Sara"])

# -----------------------------
# isin()
# -----------------------------
print("\nAlex and Mike")
print(df[df["Name"].isin(["Alex", "Mike"])])

# -----------------------------
# between()
# -----------------------------
print("\nScores between 80 and 90")
print(df[df["Score"].between(80, 90)])