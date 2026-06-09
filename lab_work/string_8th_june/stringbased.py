attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record:", attendance)

# Validation: Attendance record should not be empty
if len(attendance) > 0:

    # 1. Count Present and Absent Days
    present = 0
    absent = 0

    for ch in attendance:

        if ch == "P":      # Validation
            present += 1

        elif ch == "A":      # Validation
            absent += 1

    print("Present Days:", present)
    print("Absent Days:", absent)

    # 2. Calculate Attendance Percentage
    percentage = (present / len(attendance)) * 100

    print("Attendance Percentage:", round(percentage, 2), "%")

    # 3. Longest Consecutive Present Streak
    current_p = 0
    longest_p = 0

    for ch in attendance:

        if ch == "P":      # Validation
            current_p += 1

            if current_p > longest_p:      # Validation
                longest_p = current_p

        else:
            current_p = 0

    print("Longest Present Streak:", longest_p)

    # 4. Longest Consecutive Absent Streak
    current_a = 0
    longest_a = 0

    for ch in attendance:

        if ch == "A":      # Validation
            current_a += 1

            if current_a > longest_a:      # Validation
                longest_a = current_a

        else:
            current_a = 0

    print("Longest Absent Streak:", longest_a)

    # 5. Attendance Status
    if percentage < 75:      # Validation
        print("Attendance Status: Below 75%")

    else:
        print("Attendance Status: Above 75%")

else:
    print("Attendance Record is Empty")