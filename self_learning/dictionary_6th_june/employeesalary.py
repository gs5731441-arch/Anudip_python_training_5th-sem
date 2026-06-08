salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# 1. Display employees earning above ₹60,000
print("Employees Earning Above ₹60,000:")

for emp_id, sal in salary.items():

    if sal > 60000:      # Validation
        print(emp_id, ":", sal)

# 2. Count employees earning below ₹40,000
count = 0

for sal in salary.values():

    if sal < 40000:      # Validation
        count += 1

print("\nEmployees Earning Below ₹40,000 =", count)

# 3. Find the highest-paid employee
first = True

for emp_id, sal in salary.items():

    if first == True:
        highest_emp = emp_id
        highest_salary = sal
        first = False

    elif sal > highest_salary:     # Validation
        highest_salary = sal
        highest_emp = emp_id

print("\nHighest Paid Employee:")
print(highest_emp, ":", highest_salary)

# 4. Create list of employees eligible for bonus
bonus_list = []

for emp_id, sal in salary.items():

    if sal > 50000:      # Validation
        bonus_list.append(emp_id)

print("\nEmployees Eligible for Bonus:")
print(bonus_list)

# 5. Calculate average salary
total_salary = 0

for sal in salary.values():

    if sal >= 0:      # Validation
        total_salary += sal

average_salary = total_salary / len(salary)

print("\nAverage Salary =", average_salary)
   