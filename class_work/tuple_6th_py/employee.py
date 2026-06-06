employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Employees scoring 80 or above
print("Employees Scoring 80 or Above:")
for emp_id, name, score in employees:
    if score >= 80:
        print(emp_id, name, score)

# 2. Count employees needing improvement
count = 0
for emp_id, name, score in employees:
    if score < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find highest performer
highest = employees[0]

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

# 4. List of employees scoring above 75
high_performers = []

for emp_id, name, score in employees:
    if score > 75:
        high_performers.append(name)

print("\nHigh Performers:")
print(high_performers)

# 5. Performance categories
print("\nPerformance Categories:")

for emp_id, name, score in employees:
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(name, "->", category)