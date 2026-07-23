# Lesson 10: Sorting Data

import pandas as pd

# --------------------------------
# Create DataFrame
# --------------------------------

data = {
    "Name": ["Alex", "Sara", "John", "Mike"],
    "Age": [22, 21, 23, 22],
    "Score": [95, 88, 76, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# --------------------------------
# Sort by Score (Ascending)
# --------------------------------

print("\nSort by Score (Ascending):")
print(df.sort_values(by="Score"))

# --------------------------------
# Sort by Score (Descending)
# --------------------------------

print("\nSort by Score (Descending):")
print(df.sort_values(by="Score", ascending=False))

# --------------------------------
# Sort by Score and Age
# --------------------------------

print("\nSort by Score and Age:")
print(df.sort_values(by=["Score", "Age"]))

# --------------------------------
# Different sorting order
# --------------------------------

print("\nScore Descending, Age Ascending:")
print(df.sort_values(by=["Score", "Age"],
                     ascending=[False, True]))

# --------------------------------
# Sort by Index
# --------------------------------

print("\nSort by Index:")
print(df.sort_index())

# --------------------------------
# Reset Index
# --------------------------------

sorted_df = df.sort_values(by="Score")

sorted_df = sorted_df.reset_index(drop=True)

print("\nAfter Resetting Index:")
print(sorted_df)