# ==========================
# Lesson 12: Reading Excel
# ==========================

import pandas as pd


# Read Excel file
df = pd.read_excel(
    "students.xlsx",
    engine="openpyxl"
)

print("Dataset:")
print(df)


# First rows
print("\nFirst 5 Rows:")
print(df.head())


# Last rows
print("\nLast 5 Rows:")
print(df.tail())


# Shape
print("\nShape:")
print(df.shape)


# Columns
print("\nColumns:")
print(df.columns)


# Info
print("\nInfo:")
df.info()


# Statistics
print("\nStatistics:")
print(df.describe())


# Select columns
basic_info = pd.read_excel(
    "students.xlsx",
    usecols=[
        "StudentID",
        "FirstName",
        "LastName",
        "Grade",
        "GPA",
        "Major"
    ]
)

print("\nSelected Columns:")
print(basic_info)


# Read first 10 rows
first_students = pd.read_excel(
    "students.xlsx",
    nrows=10
)

print("\nFirst 10 Students:")
print(first_students)


# Read specific sheet
# Example:
# df2 = pd.read_excel(
#     "students.xlsx",
#     sheet_name="Sheet1"
# )