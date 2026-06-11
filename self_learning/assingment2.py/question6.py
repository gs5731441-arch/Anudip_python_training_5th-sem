# Student Resume Analyzer

resume = """
Name: Gopal Thakur

Email: gopal123@gmail.com
Phone: 9876543210

Skills:
Python SQL React Java Communication Python SQL Java

Education:
Bachelor of Computer Applications

Projects:
Library Management System
Student Management System
Online Examination System

Achievements:
Python Certification
Coding Competition Winner
Best Project Award
"""

# Total Words
words = resume.split()
total_words = len(words)

# Total Characters
total_characters = len(resume)

# Extract Emails
emails = []

for word in words:
    if "@" in word and "." in word:
        emails.append(word)

# Extract Phone Numbers
phones = []

for word in words:
    if word.isdigit() and len(word) == 10:
        phones.append(word)

# Skill List
skills = ["Python", "SQL", "React", "Java", "Communication"]

# Skill Frequency Report
skill_freq = {}

for skill in skills:

    count = resume.count(skill)

    if count > 0:
        skill_freq[skill] = count

# Most Frequent Skill
most_skill = ""
max_skill_count = 0

for skill in skill_freq:

    if skill_freq[skill] > max_skill_count:
        max_skill_count = skill_freq[skill]
        most_skill = skill

# Word Frequency Dictionary
freq = {}

for word in words:

    word = word.lower()

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Repeated Keywords
repeated_keywords = []

for word in freq:

    if freq[word] > 1:
        repeated_keywords.append(word)

# Most Frequently Used Word
most_word = ""
max_word_count = 0

for word in freq:

    if freq[word] > max_word_count:
        max_word_count = freq[word]
        most_word = word

# Duplicate Skills
duplicate_skills = []

for skill in skill_freq:

    if skill_freq[skill] > 1:
        duplicate_skills.append(skill)

# Top 5 Keywords
top_keywords = []

for word in freq:

    if freq[word] > 1:
        top_keywords.append(word)

# Output
print("========== RESUME ANALYSIS REPORT ==========")

print("Total Words :", total_words)
print("Total Characters :", total_characters)

print("\nEmail Found :", len(emails))
for email in emails:
    print(email)

print("\nPhone Numbers Found :", len(phones))
for phone in phones:
    print(phone)

print("\nMost Frequent Skill :", most_skill)

print("\nSkill Frequency Report")
for skill in skill_freq:
    print(skill, ":", skill_freq[skill])

print("\nDuplicate Skills")
for skill in duplicate_skills:
    print(skill)

print("\nRepeated Keywords")
for word in repeated_keywords:
    print(word)

print("\nMost Frequently Used Word :", most_word)

print("\nTop 5 Keywords")
count = 0

for word in top_keywords:
    print(word)
    count += 1

    if count == 5:
        break

print("\n========== SUMMARY DASHBOARD ==========")
print("Total Words :", total_words)
print("Total Characters :", total_characters)
print("Email Found :", len(emails))
print("Phone Numbers Found :", len(phones))
print("Most Frequent Skill :", most_skill)
print("Most Frequently Used Word :", most_word)