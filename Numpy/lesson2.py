import numpy as np

# 1. Create array from list
numbers = np.array([10, 20, 30, 40, 50])

print("Array:")
print(numbers)


# 2. Create zeros array
zeros = np.zeros(5)

print("\nZeros:")
print(zeros)


# 3. Create ones matrix
ones = np.ones((3, 3))

print("\nOnes:")
print(ones)


# 4. Create sequence
sequence = np.arange(0, 20, 2)

print("\nArange:")
print(sequence)


# 5. Create evenly spaced numbers
space = np.linspace(0, 10, 5)

print("\nLinspace:")
print(space)


# 6. Create identity matrix
identity = np.eye(3)

print("\nIdentity Matrix:")
print(identity)