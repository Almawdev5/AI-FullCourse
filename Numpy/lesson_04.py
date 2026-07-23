import numpy as np

# -------------------------
# 1D ARRAY
# -------------------------

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)

print("\nFirst Element:")
print(numbers[0])

print("\nThird Element:")
print(numbers[2])

print("\nLast Element:")
print(numbers[-1])

print("\nFirst Three Elements:")
print(numbers[:3])

print("\nLast Three Elements:")
print(numbers[-3:])

print("\nElements from Index 1 to 3:")
print(numbers[1:4])

print("\nEvery Second Element:")
print(numbers[::2])

print("\nReverse Array:")
print(numbers[::-1])

# -------------------------
# 2D ARRAY
# -------------------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nMatrix:")
print(matrix)

print("\nElement (1,1):")
print(matrix[1,1])

print("\nElement (2,2):")
print(matrix[2,2])

print("\nFirst Row:")
print(matrix[0])

print("\nSecond Row:")
print(matrix[1])

print("\nFirst Column:")
print(matrix[:,0])

print("\nSecond Column:")
print(matrix[:,1])

print("\nLast Column:")
print(matrix[:,-1])

print("\nFirst Two Rows:")
print(matrix[:2])

print("\nFirst Two Columns:")
print(matrix[:,:2])

# Modify values
matrix[0,2] = 999

print("\nUpdated Matrix:")
print(matrix)
