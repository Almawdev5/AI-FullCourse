# Lesson 7: Creating DataFrames


import pandas as pd
import numpy as np



# --------------------------------
# 1. DataFrame from Dictionary
# --------------------------------

data = {

    "Name": ["Alex","Sara","John"],

    "Age": [22,21,23],

    "Score": [95,88,76]

}


df1 = pd.DataFrame(data)


print("DataFrame from Dictionary:")
print(df1)



# --------------------------------
# 2. DataFrame from List
# --------------------------------


students = [

    ["Mike",24,90],

    ["Anna",20,85],

    ["David",22,92]

]


df2 = pd.DataFrame(
    students,
    columns=["Name","Age","Score"]
)


print("\nDataFrame from List:")
print(df2)



# --------------------------------
# 3. DataFrame from NumPy array
# --------------------------------


array = np.array([

    [1,90],

    [2,85],

    [3,95]

])


df3 = pd.DataFrame(
    array,
    columns=["ID","Score"]
)


print("\nDataFrame from NumPy:")
print(df3)



# --------------------------------
# 4. Custom Index
# --------------------------------


df4 = pd.DataFrame(

    data,

    index=[
        "Student1",
        "Student2",
        "Student3"
    ]

)


print("\nCustom Index:")
print(df4)



# --------------------------------
# 5. Adding Column
# --------------------------------


df1["Grade"] = [
    "A",
    "B",
    "C"
]


print("\nAfter adding Grade:")
print(df1)



# --------------------------------
# DataFrame Attributes
# --------------------------------


print("\nColumns:")
print(df1.columns)


print("\nIndex:")
print(df1.index)


print("\nShape:")
print(df1.shape)


print("\nValues:")
print(df1.values)