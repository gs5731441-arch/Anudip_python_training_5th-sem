attendance = {}

# Input attendance of 30 students
for i in range(30):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")

    attendance[roll_no] = status

# Display present students
print("\nStudents who are Present:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)