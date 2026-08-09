"""
Exercise: Student Score Dictionary
Student: Bishal Khadka
Day: 2
"""

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# display the student scores
for student, score in student_scores.items():
    print(f'{student}: {score}')

# dictionary of student who passed the exam (score >= 60)
passed_students = {student: score for student, score in student_scores.items() if score >= 60}
print(f'Passed Students: {passed_students}')

# print the highest score with student name
highest_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_student]
print(f'Highest Student: {highest_student}, Score: {highest_score}')

average_score = sum(student_scores.values()) / len(student_scores)
print(f'Average Score: {average_score: .2f}')

# Output:
'''
Anisha: 78
Ravi: 55
Maya: 92
Sagar: 61
Nima: 48
Passed Students: {'Anisha': 78, 'Maya': 92, 'Sagar': 61}
Highest Student: Maya, Score: 92
Average Score:  66.80
'''