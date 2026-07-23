import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

print("\nAdd 5:")
print(arr + 5)

print("\nSubtract 5:")
print(arr - 5)

print("\nMultiply by 2:")
print(arr * 2)

print("\nDivide by 2:")
print(arr / 2)

print("\nSquare:")
print(arr ** 2)

arr2 = np.array([1, 2, 3, 4, 5])

print("\nArray Addition:")
print(arr + arr2)

print("\nComparison (>25):")
print(arr > 25)

print("\nSquare Root:")
print(np.sqrt(arr))

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))