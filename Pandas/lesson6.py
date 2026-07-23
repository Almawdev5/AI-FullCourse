# Lesson 6: Introduction to Pandas DataFrame


import pandas as pd



# --------------------------------
# Creating a DataFrame
# --------------------------------

data = {

    "Name": [
        "Alex",
        "Sara",
        "John"
    ],

    "Age": [
        22,
        21,
        23
    ],

    "Score": [
        95,
        88,
        76
    ]

}



# Convert dictionary to DataFrame

df = pd.DataFrame(data)



print("Student DataFrame:")
print(df)



# --------------------------------
# Selecting a column
# --------------------------------

print("\nName column:")

print(df["Name"])



# --------------------------------
# Dataset information
# --------------------------------

print("\nDataFrame information:")

df.info()



# --------------------------------
# Dataset shape
# --------------------------------

print("\nShape of DataFrame:")

print(df.shape)



# --------------------------------
# First rows
# --------------------------------

print("\nFirst rows:")

print(df.head())



# --------------------------------
# Last rows
# --------------------------------

print("\nLast rows:")

print(df.tail())