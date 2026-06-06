employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# List for employees earning above 50000
high_salary = []

# Highest paid employee
highest_name = employees[0][0]
highest_salary = employees[0][1]

# Total salary expenditure
total_salary = 0

# Count employees below 40000
count_below_40000 = 0

for name, salary in employees:

    # Employees earning above 50000
    if salary > 50000:
        high_salary.append(name)

    # Highest paid employee
    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

    # Total salary
    total_salary += salary

    # Count employees below 40000
    if salary < 40000:
        count_below_40000 += 1

print("Employees earning above ₹50,000:", high_salary)
print("Highest Paid Employee:", highest_name, "-", highest_salary)
print("Total Salary Expenditure:", total_salary)
print("Employees earning below ₹40,000:", count_below_40000)