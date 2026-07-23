# ==========================
# Lesson 13: Reading JSON
# ==========================

import pandas as pd


# Read JSON file

df = pd.read_json(
    "students.json"
)

print("Dataset:")
print(df)


# First rows

print("\nFirst Rows:")
print(df.head())


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


# JSON data directly

data = [
    {
        "Name":"Alex",
        "Age":22,
        "Score":95
    },
    {
        "Name":"Sara",
        "Age":21,
        "Score":88
    }
]


df2 = pd.DataFrame(data)


print("\nDataFrame from JSON Object:")
print(df2)


# Nested JSON

nested_data = [
    {
        "Name":"Alex",
        "Details":{
            "Age":22,
            "Score":95
        }
    }
]


nested_df = pd.json_normalize(
    nested_data
)


print("\nFlattened JSON:")
print(nested_df)