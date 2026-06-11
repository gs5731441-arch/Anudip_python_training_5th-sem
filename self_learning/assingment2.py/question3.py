# Chat Message Analytics Dashboard

messages = [
    "hello how are you",
    "i am fine thank you",
    "python is very easy",
    "hello everyone",
    "data science is interesting",
    "machine learning is powerful",
    "good morning friends",
    "have a nice day",
    "artificial intelligence is growing",
    "practice makes a man perfect",
    "coding improves problem solving",
    "welcome to python class",
    "learning new skills is important",
    "hard work leads to success",
    "never stop learning",
    "python programming is fun",
    "good evening everyone",
    "stay focused and motivated",
    "hello friends welcome",
    "education changes lives"
]

total_words_all = 0
longest_message = messages[0]
shortest_message = messages[0]

all_words = []

for msg in messages:

    print("\nMessage :", msg)

    words = msg.split()

    # Total words
    total_words = len(words)
    print("Total Words :", total_words)

    # Total characters
    total_characters = len(msg)
    print("Total Characters :", total_characters)

    # Vowels and Consonants
    vowels = 0
    consonants = 0

    for ch in msg.lower():

        if ch.isalpha():

            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels :", vowels)
    print("Consonants :", consonants)

    # Longest word
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print("Longest Word :", longest_word)

    # Shortest word
    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    print("Shortest Word :", shortest_word)

    # Word Frequency Dictionary
    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("Word Frequency :", frequency)

    # Repeated Words
    repeated = []

    for word in frequency:

        if frequency[word] > 1:
            repeated.append(word)

    print("Repeated Words :", repeated)

    # Words Starting With Vowels
    vowel_words = []

    for word in words:

        if word[0].lower() in "aeiou":
            vowel_words.append(word)

    print("Words Starting With Vowels :", vowel_words)

    # Words Longer Than 5 Characters
    long_words = []

    for word in words:

        if len(word) > 5:
            long_words.append(word)

    print("Words Longer Than 5 Characters :", long_words)

    # Store all words for final report
    for word in words:
        all_words.append(word)

    total_words_all += total_words

    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg


# Overall Word Frequency
overall_frequency = {}

for word in all_words:

    if word in overall_frequency:
        overall_frequency[word] += 1
    else:
        overall_frequency[word] = 1

# Most Frequently Used Word
most_word = ""
max_count = 0

for word in overall_frequency:

    if overall_frequency[word] > max_count:
        max_count = overall_frequency[word]
        most_word = word

# Average Words Per Message
average_words = total_words_all / len(messages)

# Final Report
print("\n")
print("========== CHAT ANALYTICS REPORT ==========")

print("Most Frequently Used Word :", most_word)

print("Longest Message :")
print(longest_message)

print("Shortest Message :")
print(shortest_message)

print("Average Words Per Message :", average_words)