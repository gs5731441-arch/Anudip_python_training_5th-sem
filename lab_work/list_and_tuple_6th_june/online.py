correct = ('A', 'C', 'B', 'D', 'A')      # Tuple
student = ['A', 'B', 'B', 'D', 'C']      # List

score = 0
correct_count = 0
wrong_count = 0

# List to store incorrect question numbers
wrong_questions = []

for i in range(len(correct)):

    if correct[i] == student[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1
        wrong_questions.append(i + 1)

# Percentage
percentage = (score / len(correct)) * 100

print("Score:", score)
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Incorrect Question Numbers:", wrong_questions)
print("Percentage:", percentage)

# Pass/Fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")