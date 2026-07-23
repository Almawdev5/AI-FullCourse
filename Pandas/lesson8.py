# Lesson 8: DataFrame Structure

import pandas as pd

# -----------------------------
# Create a DataFrame
# -----------------------------
data = {
    "Name": ["Alex", "Sara", "John"],
    "Age": [22, 21, 23],
    "Score": [95, 88, 76]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# -----------------------------
# Select one column
# -----------------------------
print("\nName column:")
print(df["Name"])

# -----------------------------
# Select multiple columns
# -----------------------------
print("\nName and Score columns:")
print(df[["Name", "Score"]])

# -----------------------------
# Select row using loc
# -----------------------------
print("\nSecond row using loc:")
print(df.loc[1])

# -----------------------------
# Select row using iloc
# -----------------------------
print("\nFirst row using iloc:")
print(df.iloc[0])

# -----------------------------
# Select a single value
# -----------------------------
print("\nScore of Sara:")
print(df.loc[1, "Score"])

print("\nScore of Sara using iloc:")
print(df.iloc[1, 2])

# -----------------------------
# Slice rows
# -----------------------------
print("\nFirst two rows:")
print(df.iloc[0:2])