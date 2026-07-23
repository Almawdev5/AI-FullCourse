# Lesson 5: Pandas Series Operations

import pandas as pd


# Create Series

scores = pd.Series(
    [90,80,70,100],
    index=["Alex","Sara","John","Mike"]
)


print("Original Scores:")
print(scores)



# -----------------------------
# Arithmetic operations
# -----------------------------

print("\nAdding 5 points:")
print(scores + 5)


print("\nSubtracting 10 points:")
print(scores - 10)


print("\nMultiply by 2:")
print(scores * 2)



# -----------------------------
# Comparison
# -----------------------------

print("\nScores above 80:")
print(scores[scores > 80])



# -----------------------------
# Statistics
# -----------------------------

print("\nAverage:")
print(scores.mean())


print("\nTotal:")
print(scores.sum())


print("\nHighest:")
print(scores.max())


print("\nLowest:")
print(scores.min())


print("\nNumber of students:")
print(scores.count())



# -----------------------------
# Unique values
# -----------------------------

numbers = pd.Series(
    [90,90,80,70]
)

print("\nUnique values:")
print(numbers.unique())



print("\nValue counts:")
print(numbers.value_counts())



# -----------------------------
# Apply function
# -----------------------------

print("\nConvert to percentage:")

print(
    scores.apply(
        lambda x: x/100
    )
)



# -----------------------------
# Sorting
# -----------------------------

print("\nSorted ascending:")
print(scores.sort_values())


print("\nSorted descending:")
print(
    scores.sort_values(
        ascending=False
    )
)