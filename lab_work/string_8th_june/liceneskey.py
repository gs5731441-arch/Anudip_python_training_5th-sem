license_key = "ABCD-EFGH-IJKL-MNOP"

print("License Key:", license_key)

# Validation: Key should not be empty
if len(license_key) > 0:

    # 1 & 6. Create List of Groups
    groups = license_key.split("-")

    print("Groups:", groups)
    print("Number of Groups:", len(groups))

    # 2. Verify Each Group Contains Exactly 4 Characters
    valid = True

    if len(groups) != 4:      # Validation
        valid = False

    for group in groups:

        if len(group) != 4:      # Validation
            valid = False

    # 3. Count Total Letters
    letter_count = 0

    for ch in license_key:

        if ch.isalpha():      # Validation
            letter_count += 1

    print("Total Letters:", letter_count)

    # 4. Count Vowels
    vowel_count = 0

    for ch in license_key:

        if ch.upper() in "AEIOU":      # Validation
            vowel_count += 1

    print("Total Vowels:", vowel_count)

    # 5. Remove Hyphens
    merged_key = license_key.replace("-", "")
    print("Merged Key:", merged_key)

    # 7. Display Status
    if valid == True:
        print("License Key Status: Valid")

    else:
        print("License Key Status: Invalid")

else:
    print("License Key is Empty")