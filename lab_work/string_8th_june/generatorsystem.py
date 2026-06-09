name = "Rahul Sharma"

print("Original Name:", name)

# Validation: Name should not be empty
if len(name) > 0:

    # 1. Remove Spaces
    username = name.replace(" ", "")

    # 2. Convert to Lowercase
    username = username.lower()

    # 3. Append Current Year
    username = username + "2026"

    print("Generated Username:", username)

    # 4. If Length Exceeds 12, Keep First 12 Characters
    if len(username) > 12:      # Validation
        short_username = username[:12]
    else:
        short_username = username

    # 5 & 6. Count Vowels and Consonants
    vowels = 0
    consonants = 0

    for ch in username:

        if ch.isalpha():      # Validation

            if ch in "aeiou":      # Validation
                vowels += 1

            else:
                consonants += 1

    # 7. Display Statistics
    print("Username Length:", len(username))
    print("Vowels:", vowels)
    print("Consonants:", consonants)

    print("Status: Username Generated Successfully")

else:
    print("Invalid Name")