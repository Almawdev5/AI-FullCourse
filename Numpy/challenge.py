import numpy as np

# 1. Create your marks array
marks = np.array([80, 90, 75, 88, 95])

print("Marks:")
print(marks)


# 2. Add 5 bonus marks
print("\nBonus Marks:")
print(marks + 5)


# 3. Create zeros
print("\nZeros:")
print(np.zeros(5))


# 4. Create 3x3 matrix of 7
print("\nMatrix:")
print(np.full((3,3), 7))


# 5. Create numbers 0 to 50 step 5
print("\nRange:")
print(np.arange(0, 51, 5))


# 6. Create 5 values between 1 and 10
print("\nLinspace:")
print(np.linspace(1, 10, 5))