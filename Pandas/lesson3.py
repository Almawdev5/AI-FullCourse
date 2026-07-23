# Lesson 3: Creating Pandas Series

import pandas as pd
import numpy as np


# -----------------------------
# 1. Series from a list
# -----------------------------

scores = pd.Series([95, 88, 76])

print("Series from list:")
print(scores)



# -----------------------------
# 2. Series with custom index
# -----------------------------

student_scores = pd.Series(
    [95,88,76],
    index=["Alex","Sara","John"]
)

print("\nCustom index Series:")
print(student_scores)



# -----------------------------
# 3. Series from dictionary
# -----------------------------

students = {
    "Alex":95,
    "Sara":88,
    "John":76
}

dictionary_series = pd.Series(students)

print("\nSeries from dictionary:")
print(dictionary_series)



# -----------------------------
# 4. Series from NumPy array
# -----------------------------

numbers = np.array([10,20,30])

numpy_series = pd.Series(numbers)

print("\nSeries from NumPy array:")
print(numpy_series)



# -----------------------------
# 5. Single value Series
# -----------------------------

attendance = pd.Series(
    100,
    index=["Alex","Sara","John"]
)

print("\nSingle value Series:")
print(attendance)



# -----------------------------
# 6. Missing values
# -----------------------------

scores_with_nan = pd.Series(
    [95,88,None,76]
)

print("\nSeries with missing value:")
print(scores_with_nan)



# Check missing values

print("\nChecking missing values:")
print(scores_with_nan.isnull())



# Fill missing values

print("\nAfter filling missing values:")
print(scores_with_nan.fillna(0))