message = "Python is awesome and Python is easy to learn"

print("Message:", message)

# 1. Count Total Characters
char_count = len(message)
print("Total Characters:", char_count)

# 2. Count Total Words
words = message.split()

word_count = len(words)
print("Total Words:", word_count)

# 3. Find Longest Word
longest_word = words[0]

for word in words:

    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)

# 4. Find Shortest Word
shortest_word = words[0]

for word in words:

    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)

# 5. Count Occurrences of Python
python_count = 0

for word in words:

    if word == "Python":
        python_count += 1

print("Occurrences of Python:", python_count)

# 6. Create List of Words Having More Than 4 Characters
long_words = []

for word in words:

    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:", long_words)

# 7. Display Words Starting With a Vowel
vowel_words = []

for word in words:

    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel:", vowel_words)

# 8. Count Vowels and Consonants
vowels = 0
consonants = 0

for ch in message:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)