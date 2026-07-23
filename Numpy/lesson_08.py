import numpy as np

# Random decimals
print("Random Decimals:")
print(np.random.rand(5))

# Random integers
print("\nRandom Integers:")
print(np.random.randint(1,11,5))

# Normal distribution
print("\nNormal Distribution:")
print(np.random.randn(5))

# Random choice
colors = ["Red", "Blue", "Green", "Black"]

print("\nRandom Color:")
print(np.random.choice(colors))

# Seed
np.random.seed(42)

print("\nSeed Example:")
print(np.random.randint(1,11,5))

# Shuffle
numbers = np.array([1,2,3,4,5])

np.random.shuffle(numbers)

print("\nShuffled Array:")
print(numbers)