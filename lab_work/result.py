# Program to calculate Total Marks, Percentage, Grade
# and Number of Failed Subjects

total = 0
fail_count = 0

for i in range(1, 6):
    marks = float(input("Enter marks of Subject " + str(i) + ": "))

    total += marks

    if marks < 40:
        fail_count += 1

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)
print("Number of Subjects Failed =", fail_count)