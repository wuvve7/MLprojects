import numpy as np
import matplotlib.pyplot as plt

student_scores = np.random.randint(50, 100, size=100)

mean_score = np.mean(student_scores)
median_score = np.median(student_scores)
std_dev_score = np.std(student_scores)
min_score = np.min(student_scores)
max_score = np.max(student_scores)

print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation: {std_dev_score:.2f}")
print(f"Minimum Score: {min_score}")
print(f"Maximum Score: {max_score}")

plt.figure(figsize=(10, 6))
plt.hist(student_scores, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Student Scores')
plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(student_scores, vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue'))
plt.title('Box Plot of Student Scores')
plt.xlabel('Scores')
plt.show()

above_average = student_scores[student_scores > mean_score]
print(f"\nScores above the average score ({mean_score:.2f}):")
print(above_average)
num_above_average = len(above_average)
print(f"\nNumber of students who scored above average: {num_above_average}")
