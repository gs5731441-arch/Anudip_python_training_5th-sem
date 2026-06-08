quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# 1. Display students scoring 15 or above
print("Students Scoring 15 or Above:")

for student, score in quiz_scores.items():

    if score >= 15:      # Validation
        print(student, ":", score)

# 2. Count students scoring below 10
count = 0

for score in quiz_scores.values():

    if score < 10:      # Validation
        count += 1

print("\nStudents Scoring Below 10 =", count)

# 3. Find the top performer
first = True

for student, score in quiz_scores.items():

    if first == True:
        top_student = student
        top_score = score
        first = False

    elif score > top_score:      # Validation
        top_score = score
        top_student = student

print("\nTop Performer:")
print(top_student, ":", top_score)

# 4. Create a list of students who passed
passed_students = []

for student, score in quiz_scores.items():

    if score >= 10:      # Validation
        passed_students.append(student)

print("\nPassed Students:")
print(passed_students)

# 5. Calculate the class average
total = 0

for score in quiz_scores.values():

    if score >= 0:      # Validation
        total += score

average = total / len(quiz_scores)

print("\nClass Average =", average)