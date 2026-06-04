# Program to record attendance of 30 students using while loop

present = 0
absent = 0
count = 1

while count <= 30:
    status = input("Enter P for Present or A for Absent: ")

    if status == "P" or status == "p":
        present += 1
    elif status == "A" or status == "a":
        absent += 1
    else:
        print("Invalid Input!")
        continue

    count += 1

print("\nAttendance Report")
print("Total Students =", 30)
print("Present Students =", present)
print("Absent Students =", absent)