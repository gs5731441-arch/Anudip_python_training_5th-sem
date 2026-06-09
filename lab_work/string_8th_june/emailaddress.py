email = "rahul.sharma2026@gmail.com"

print("Email:", email)

# Validation: Check email is not empty
if len(email) > 0:

    # 1. Extract Username
    username = email[:email.index("@")]
    print("Username:", username)

    # 2. Extract Domain Name
    domain_part = email[email.index("@") + 1:]

    domain = domain_part[:domain_part.index(".")]
    print("Domain:", domain)

    # 3. Extract Extension
    extension = domain_part[domain_part.index(".") + 1:]
    print("Extension:", extension)

    # 4. Count Digits in Username
    digit_count = 0

    for ch in username:

        if ch.isdigit():      # Validation
            digit_count += 1

    print("Digits Found:", digit_count)

    # 5. Count Special Characters
    special_count = 0

    for ch in email:

        if not ch.isalnum() and ch != "@":      # Validation
            special_count += 1

    print("Special Characters Found:", special_count)

    # 6. Email Validation
    valid = True

    # Exactly one @
    if email.count("@") != 1:      # Validation
        valid = False

    # At least one . after @
    at_pos = email.find("@")

    if "." not in email[at_pos + 1:]:      # Validation
        valid = False

    # 7. Display Status
    if valid == True:
        print("Email Status: Valid")

    else:
        print("Email Status: Invalid")

else:
    print("Email is Empty")