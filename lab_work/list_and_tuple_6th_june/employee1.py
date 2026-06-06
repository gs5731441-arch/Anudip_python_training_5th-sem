employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Employees earning above 50000
print("Employees earning above ₹50,000:")
for name, salary in employees:
    if salary > 50000:
        print(name, "-", salary)

# Highest-paid employee
highest_name = employees[0][0]
highest_salary = employees[0][1]

for name, salary in employees:
    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print("\nHighest Paid Employee:")
print(highest_name, "-", highest_salary)

# Total salary expenditure
total_salary = 0

for name, salary in employees:
    total_salary += salary

print("\nTotal Salary Expenditure:", total_salary)

# Count employees earning below 40000
count = 0

for name, salary in employees:
    if salary < 40000:
        count += 1

print("Employees earning below ₹40,000:", count)