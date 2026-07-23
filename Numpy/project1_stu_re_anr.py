import numpy as np

# Student names
students = np.array(["Alex", "John", "Sara", "Mike", "Helen"])

# Marks: Math, Physics, English
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 88, 92],
    [60, 75, 70],
    [88, 91, 84]
])

print("========== STUDENT RESULT ANALYZER ==========\n")

# Display marks
print("Students:")
print(students)

print("\nMarks:")
print(marks)

# Overall statistics
print("\n----- Overall Statistics -----")
print("Average Mark:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Median Mark:", np.median(marks))

# Subject-wise averages
print("\n----- Subject Averages -----")
subjects = ["Math", "Physics", "English"]

for i in range(3):
    print(f"{subjects[i]} Average: {np.mean(marks[:, i]):.2f}")

# Student averages
student_avg = np.mean(marks, axis=1)

print("\n----- Student Averages -----")
for i in range(len(students)):
    print(f"{students[i]}: {student_avg[i]:.2f}")

# Pass / Fail
print("\n----- Pass / Fail -----")
passed = student_avg >= 75

for i in range(len(students)):
    if passed[i]:
        print(f"{students[i]}: PASS")
    else:
        print(f"{students[i]}: FAIL")

# Bonus marks using broadcasting
bonus = np.array([2, 3, 1])

new_marks = marks + bonus

print("\n----- Marks After Bonus -----")
print(new_marks)

# Updated averages
new_avg = np.mean(new_marks, axis=1)

print("\n----- Updated Student Averages -----")
for i in range(len(students)):
    print(f"{students[i]}: {new_avg[i]:.2f}")

# Top student
top_index = np.argmax(new_avg)

print("\n----- Top Student -----")
print(f"{students[top_index]} with an average of {new_avg[top_index]:.2f}")

print("\n========== END OF REPORT ==========")