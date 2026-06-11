# Password Security Analyzer

passwords = [
    "Password123!",
    "hello123",
    "WELCOME@2025",
    "Admin#45",
    "python",
    "Secure$Pass99",
    "My Password1",
    "Qwerty@123",
    "abcABC123",
    "Strong!Pass2025",
    "Test1234",
    "User@789",
    "Data#Science1",
    "Cyber$Security99",
    "Pass@Word123"
]

strong = 0
medium = 0
weak = 0

for password in passwords:

    upper = 0
    lower = 0
    digit = 0
    special = 0
    vowel = 0
    consonant = 0

    for ch in password:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digit += 1

        else:
            special += 1

        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowel += 1
            else:
                consonant += 1

    # Length Check
    if len(password) >= 8:
        length_ok = True
    else:
        length_ok = False

    # Space Check
    if " " in password:
        space = True
    else:
        space = False

    # Strength Check
    if length_ok and upper > 0 and lower > 0 and digit > 0 and special > 0 and not space:
        strength = "Strong"
        strong += 1

    elif length_ok and (upper > 0 or lower > 0) and digit > 0:
        strength = "Medium"
        medium += 1

    else:
        strength = "Weak"
        weak += 1

    # Repeated Characters
    repeated = []

    for ch in password:
        if password.count(ch) > 1 and ch not in repeated:
            repeated.append(ch)

    # Most Frequent Character
    max_count = 0
    most_char = ""

    for ch in password:
        if password.count(ch) > max_count:
            max_count = password.count(ch)
            most_char = ch

    print("\nPassword:", password)
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)
    print("Digits:", digit)
    print("Special Characters:", special)
    print("Minimum Length (8):", length_ok)
    print("Contains Space:", space)
    print("Strength:", strength)
    print("Repeated Characters:", repeated)
    print("Vowels:", vowel)
    print("Consonants:", consonant)
    print("Most Frequent Character:", most_char)

# Final Report

print("\n----- SECURITY REPORT -----")
print("Total Passwords Analyzed:", len(passwords))
print("Strong Passwords:", strong)
print("Medium Passwords:", medium)
print("Weak Passwords:", weak)