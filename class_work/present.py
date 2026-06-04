# Program to record attendance of 30 students
# and count Present and Absent students

present = 0
absent = 0
count = 1

while count <= 30:
    status = input(f"Student {count} (P/A): ")

    if status == "P" or status == "p":
        present += 1
    elif status == "A" or status == "a":
        absent += 1
    else:
        print("Invalid Input! Enter P for Present or A for Absent.")
        continue

    count += 1

print("Attendance Report")
print("Total Students =", 30)
print("Present Students =", present)
print("Absent Students =", absent)