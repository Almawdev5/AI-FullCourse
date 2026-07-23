# ==========================
# Lesson 14: Exploring Data
# ==========================

import pandas as pd


# Load online CSV

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


df = pd.read_csv(url)


# View dataset

print("Dataset:")
print(df)


# First rows

print("\nFirst Rows:")
print(df.head())


# Last rows

print("\nLast Rows:")
print(df.tail())


# Shape

print("\nShape:")
print(df.shape)


# Columns

print("\nColumns:")
print(df.columns)


# Data types

print("\nData Types:")
print(df.dtypes)


# Info

print("\nInfo:")
df.info()


# Statistics

print("\nStatistics:")
print(df.describe())


# Missing values

print("\nMissing Values:")
print(df.isnull().sum())


# Duplicate rows

print("\nDuplicates:")
print(df.duplicated().sum())


# Unique values

print("\nSpecies:")
print(df["species"].unique())


# Count values

print("\nSpecies Count:")
print(df["species"].value_counts())


# Numerical columns

print("\nNumerical Columns:")
print(
    df.select_dtypes(
        include="number"
    ).columns
)


# Average values

print("\nAverage Sepal Length:")
print(df["sepal_length"].mean())


# Highest value

print("\nMaximum Sepal Length:")
print(df["sepal_length"].max())


# Group analysis

print("\nAverage By Species:")
print(
    df.groupby("species").mean(
        numeric_only=True
    )
)