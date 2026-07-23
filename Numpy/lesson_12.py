import numpy as np

hours = np.array([1,2,3,4,5])
scores = np.array([50,60,70,80,90])

print("Correlation:")
print(np.corrcoef(hours,scores))

print("\nCovariance:")
print(np.cov(hours,scores))

marks = np.array([70,82,95,61,88])

print("\nMinimum:")
print(np.min(marks))

print("\nMaximum:")
print(np.max(marks))

print("\n25th Percentile:")
print(np.percentile(marks,25))

print("\n50th Percentile:")
print(np.percentile(marks,50))

print("\n75th Percentile:")
print(np.percentile(marks,75))