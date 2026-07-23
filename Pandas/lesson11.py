# Lesson 11: Reading CSV Files

import pandas as pd

# -----------------------------
# Read CSV file
# -----------------------------

df = pd.read_csv("students.csv")

print("Dataset:")
print(df)

# -----------------------------
# First rows
# -----------------------------

print("\nFirst 3 rows:")
print(df.head(3))

# -----------------------------
# Last rows
# -----------------------------

print("\nLast 2 rows:")
print(df.tail(2))

# -----------------------------
# Shape
# -----------------------------

print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# Columns
# -----------------------------

print("\nColumns:")
print(df.columns)

# -----------------------------
# Dataset Info
# -----------------------------

print("\nDataset Information:")
df.info()

# -----------------------------
# Statistics
# -----------------------------

print("\nStatistics:")
print(df.describe())