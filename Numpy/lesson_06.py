import numpy as np

# Scalar Broadcasting
arr = np.array([10, 20, 30, 40])

print("Original Array:")
print(arr)

print("\nAdd 5:")
print(arr + 5)

print("\nMultiply by 2:")
print(arr * 2)


# 2D Broadcasting
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix:")
print(matrix)

print("\nMatrix + 10:")
print(matrix + 10)


# 1D to 2D Broadcasting
bonus = np.array([10, 20, 30])

print("\nRow Broadcasting:")
print(matrix + bonus)


# Column Broadcasting
bonus2 = np.array([
    [100],
    [200]
])

print("\nColumn Broadcasting:")
print(matrix + bonus2)