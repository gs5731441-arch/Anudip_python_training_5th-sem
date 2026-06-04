# Program to keep asking for marks until the student passes

while True:
    marks = int(input("Enter Marks: "))

    if marks >= 40:
        print("Result: Pass")
        print("Congratulations! You have cleared the assessment.")
        break
    else:
        print("Result: Fail")