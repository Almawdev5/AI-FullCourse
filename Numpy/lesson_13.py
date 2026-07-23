import numpy as np
import time

# Vectorization
arr = np.arange(1, 11)

print("Original:")
print(arr)

print("\nVectorized Multiplication:")
print(arr * 2)

# Timing
large = np.arange(1000000)

start = time.time()
large * 2
end = time.time()

print("\nExecution Time:")
print(end - start)

# Memory
a = np.array([1,2,3], dtype=np.int32)
b = np.array([1,2,3], dtype=np.int64)

print("\nint32 Memory:", a.nbytes, "bytes")
print("int64 Memory:", b.nbytes, "bytes")

# Copy
copy = a.copy()

copy[0] = 999

print("\nOriginal:", a)
print("Copy:", copy)