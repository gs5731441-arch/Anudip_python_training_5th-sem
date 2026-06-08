password = "Python@2026!"

upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digits_found = []
special_found = []

for ch in password:

    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

    elif ch.isdigit():
        digit_count += 1
        digits_found.append(ch)

    else:
        special_count += 1
        special_found.append(ch)

print("Password:", password)

print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("\nDigits Found:", digits_found)
print("Special Characters Found:", special_found)

# Password Strength Validation

if (len(password) >= 8 and
    upper_count >= 1 and
    lower_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

elif len(password) >= 8 and (digit_count >= 1 or special_count >= 1):

    strength = "Medium"

else:

    strength = "Weak"

print("\nPassword Strength:", strength)