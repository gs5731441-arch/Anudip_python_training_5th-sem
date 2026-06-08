performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")

for emp, score in performance.items():

    if score > 80:      # Validation
        print(emp)

# 2. Count employees needing improvement
improvement_count = 0

for score in performance.values():

    if score < 60:      # Validation
        improvement_count += 1

print("\nEmployees Needing Improvement =", improvement_count)

# 3. Find the top performer
first = True

for emp, score in performance.items():

    if first == True:
        top_employee = emp
        top_score = score
        first = False

    elif score > top_score:      # Validation
        top_score = score
        top_employee = emp

print("\nTop Performer:")
print(top_employee, "(", top_score, ")")

# 4. Calculate average performance score
total_score = 0

for score in performance.values():

    if score >= 0:      # Validation
        total_score += score

average_score = total_score / len(performance)

print("\nAverage Score =", average_score)

# 5. Create separate lists
excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():

    if score >= 90:      # Validation
        excellent.append(emp)

    elif score >= 75 and score <= 89:      # Validation
        good.append(emp)

    elif score >= 60 and score <= 74:      # Validation
        average.append(emp)

    else:      # Validation (score < 60)
        poor.append(emp)

print("\nExcellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)