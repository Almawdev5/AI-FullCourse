import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

# Find eigenvalues and eigenvectors
values, vectors = np.linalg.eig(A)

print("Matrix:")
print(A)

print("\nEigenvalues:")
print(values)

print("\nEigenvectors:")
print(vectors)

# Verify first eigenvector
v = vectors[:, 0]

print("\nA @ v:")
print(A @ v)

print("\nλ × v:")
print(values[0] * v)