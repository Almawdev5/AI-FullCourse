# Lesson 4: Pandas Series Indexing and Selection

import pandas as pd


# Create a Series

scores = pd.Series(
    [95,88,76],
    index=["Alex","Sara","John"]
)


print("Original Series:")
print(scores)



# -----------------------------
# Access one value
# -----------------------------

print("\nAlex score:")
print(scores["Alex"])



# Using loc

print("\nUsing loc:")
print(scores.loc["Sara"])



# Using iloc

print("\nUsing iloc:")
print(scores.iloc[0])



# -----------------------------
# Multiple values
# -----------------------------

print("\nSelecting multiple students:")
print(scores.loc[["Alex","John"]])



print("\nSelecting positions:")
print(scores.iloc[[0,2]])



# -----------------------------
# Slicing
# -----------------------------

print("\nSlicing:")
print(scores.iloc[0:2])



# -----------------------------
# Filtering
# -----------------------------

print("\nScores above 80:")

print(scores[scores > 80])



# -----------------------------
# Updating values
# -----------------------------

scores["John"] = 85

print("\nAfter updating John:")
print(scores)



# -----------------------------
# Adding new value
# -----------------------------

scores["Mike"] = 90

print("\nAfter adding Mike:")
print(scores)



# -----------------------------
# Removing value
# -----------------------------

scores.drop("Mike", inplace=True)

print("\nAfter removing Mike:")
print(scores)