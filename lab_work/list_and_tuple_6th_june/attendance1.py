attendance = ('P', 'P', 'A', 'P', 'A', 'P', 'P', 'P',
              'A', 'P', 'P', 'A', 'P', 'P', 'P')

present = 0
absent = 0

# List to store absent positions
absent_days = []

for i in range(len(attendance)):

    if attendance[i] == 'P':
        present += 1
    else:
        absent += 1
        absent_days.append(i + 1)

# Attendance Percentage
percentage = (present / len(attendance)) * 100

print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage)

# Eligibility Check
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

print("Absent on Days:", absent_days)