# Email Validation & Domain Analytics System

emails = [
    "rahul123@gmail.com",
    "priya@outlook.com",
    "anuj@company.in",
    "neha99@yahoo.com",
    "amit123@gmail.com",
    "rohit@outlook.com",
    "simran@gmail.com",
    "vikas@yahoo.com",
    "pooja@company.in",
    "deepak77@gmail.com",
    "rani@outlook.com",
    "arjun@yahoo.com",
    "sonam@company.in",
    "gopal123@gmail.com",
    "tina@outlook.com",
    "manish@gmail.com",
    "kiran@yahoo.com",
    "ajay@company.in",
    "invalid email@gmail.com",
    "test@@gmail.com"
]

gmail = 0
outlook = 0
yahoo = 0
company = 0

print("EMAIL ANALYSIS REPORT")

for email in emails:

    print("\nEmail:", email)

    # Validation
    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    if valid:

        username = email[:email.index("@")]
        domain = email[email.index("@") + 1:]

        dot_pos = domain.rfind(".")
        extension = domain[dot_pos + 1:]

        # Count digits in username
        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # Count special characters in username
        special_count = 0

        for ch in username:
            if not ch.isalpha() and not ch.isdigit():
                special_count += 1

        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)
        print("Digits in Username:", digit_count)
        print("Special Characters:", special_count)
        print("Valid Email")

        # Domain Count
        if domain == "gmail.com":
            gmail += 1

        elif domain == "outlook.com":
            outlook += 1

        elif domain == "yahoo.com":
            yahoo += 1

        elif domain == "company.in":
            company += 1

    else:
        print("Invalid Email")

# Domain Report
print("\n========== DOMAIN REPORT ==========")
print("gmail.com   ->", gmail, "users")
print("outlook.com ->", outlook, "users")
print("yahoo.com   ->", yahoo, "users")
print("company.in  ->", company, "users")