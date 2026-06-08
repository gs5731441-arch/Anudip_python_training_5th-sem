emp_id = "EMP2026ANUJ458"

# 1. Count Uppercase Letters
upper_count = 0

for ch in emp_id:

    if ch.isupper():      # Validation
        upper_count += 1

print("Uppercase Letters =", upper_count)

# 2. Count Digits
digit_count = 0

for ch in emp_id:

    if ch.isdigit():      # Validation
        digit_count += 1

print("Digits =", digit_count)

# 3. Extract Joining Year
year = emp_id[3:7]

if year.isdigit():      # Validation
    print("Joining Year =", year)

# 4. Extract Employee Name
name = emp_id[7:-3]

if name.isalpha():      # Validation
    print("Employee Name =", name)

# 5. Validate Employee ID
valid = True

# Rule 1: Starts with EMP
if emp_id[:3] != "EMP":
    valid = False

# Rule 2: Contains exactly 4 digits for year
if not emp_id[3:7].isdigit():
    valid = False

# Rule 3: Ends with exactly 3 digits
if not emp_id[-3:].isdigit():
    valid = False

# 6. Create List of Digits
digit_list = []

for ch in emp_id:

    if ch.isdigit():      # Validation
        digit_list.append(int(ch))

print("Digit List =", digit_list)

# 7. Sum of Digits
digit_sum = 0

for digit in digit_list:

    if digit >= 0:      # Validation
        digit_sum += digit

print("Sum of Digits =", digit_sum)

# 8. Display Status
if valid == True:      # Validation
    print("ID Status : Valid")

else:
    print("ID Status : Invalid")