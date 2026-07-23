import numpy as np

# Create array
arr = np.arange(1, 13)

print("Original Array:")
print(arr)

# Reshape
print("\n3 x 4 Matrix:")
print(arr.reshape(3,4))

print("\n2 x 6 Matrix:")
print(arr.reshape(2,6))

print("\nAutomatic Dimension:")
print(arr.reshape(3,-1))

# Flatten
matrix = arr.reshape(3,4)

print("\nFlatten:")
print(matrix.flatten())

# Ravel
print("\nRavel:")
print(matrix.ravel())

# Transpose
print("\nTranspose:")
print(matrix.T)