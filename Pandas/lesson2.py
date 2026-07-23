# Lesson 2: Pandas Series

# Import pandas
import pandas as pd


# Creating a Series from a list
scores = pd.Series([95, 88, 76, 90])

print("Basic Series:")
print(scores)



# Creating Series with custom index
student_scores = pd.Series(
    [95, 88, 76],
    index=["Alex", "Sara", "John"]
)

print("\nSeries with custom index:")
print(student_scores)



# Accessing values using loc (label)
print("\nAlex score:")
print(student_scores.loc["Alex"])



# Accessing values using iloc (position)
print("\nFirst score:")
print(student_scores.iloc[0])



# Series attributes

print("\nValues:")
print(student_scores.values)


print("\nIndex:")
print(student_scores.index)


print("\nData type:")
print(student_scores.dtype)



# Series operations

print("\nAdding 5 bonus points:")
print(student_scores + 5)



# Statistics

print("\nAverage score:")
print(student_scores.mean())


print("\nHighest score:")
print(student_scores.max())


print("\nLowest score:")
print(student_scores.min())


print("\nNumber of students:")
print(student_scores.count())