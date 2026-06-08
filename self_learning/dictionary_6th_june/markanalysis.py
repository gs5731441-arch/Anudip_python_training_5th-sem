marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# 1. Display students scoring 80 or above
print("Students Scoring 80 or Above:")
for name, score in marks.items():
    if score >= 80:
        print(name, ":", score)

# 2. Count failed students
failed_count = 0

for score in marks.values():
    if score < 40:
        failed_count += 1

print("\nFailed Students =", failed_count)

# 3. Find highest scorer
highest_marks = max(marks.values())

for name, score in marks.items():
    if score == highest_marks:
        print("\nHighest Scorer =", name, ":", score)

# 4. Create list of students scoring between 60 and 75
student_list = []

for name, score in marks.items():
    if score >= 60 and score <= 75:
        student_list.append(name)

print("\nStudents Scoring Between 60 and 75:")
print(student_list)

# 5. Assign grades with separate validation
print("\nGrades:")

for name, score in marks.items():

    if score >= 90 and score <= 100:
        grade = "A"

    elif score >= 75 and score <= 89:
        grade = "B"

    elif score >= 50 and score <= 74:
        grade = "C"

    elif score >= 0 and score < 50:
        grade = "F"

    else:
        grade = "Invalid Marks"

    print(name, ":", score, "Grade =", grade)