# News Article Text Analyzer

article = """
Technology is changing the world rapidly. People are using technology in education,
healthcare, business, communication, transportation and entertainment. Students are
learning programming, artificial intelligence, machine learning and data science.
Many schools and colleges are introducing digital learning platforms. Online education
allows students to learn from anywhere. Businesses are using technology to improve
productivity and customer service. Smartphones, computers and the internet have become
an important part of daily life. Technology helps people communicate quickly and
efficiently. Social media platforms connect millions of users across the world.

Healthcare organizations use technology to improve patient care and medical research.
Doctors use advanced equipment to diagnose diseases and provide treatment. Digital
records help hospitals manage patient information efficiently. Researchers use data
analysis tools to study health trends and discover new medicines. Technology also
supports remote healthcare services through online consultations.

In the business sector, companies use software systems to manage operations, sales,
marketing and customer relationships. E-commerce platforms allow businesses to reach
customers globally. Digital payment systems make transactions faster and safer.
Technology helps organizations analyze market trends and make better decisions.

Transportation systems are becoming smarter with the use of technology. Navigation
applications help drivers find the best routes. Electric vehicles are becoming more
popular because they reduce pollution. Smart traffic management systems improve road
safety and reduce congestion in cities.

Education continues to benefit from technology. Students can access online libraries,
video lectures and learning resources. Teachers use digital tools to create interactive
lessons. Technology encourages innovation, creativity and problem solving skills.
Learning new technologies improves career opportunities and professional growth.

Governments are investing in digital infrastructure to support economic development.
Technology creates new jobs and improves public services. Citizens can access
information and government services online. As technology continues to evolve, people
must learn new skills and adapt to changing environments. Technology plays a major role
in shaping the future of society and improving quality of life for people around the
world.
"""

# Total Characters
total_characters = len(article)

# Total Words
words = article.lower().split()
total_words = len(words)

# Total Sentences
total_sentences = article.count(".")

# Vowels and Consonants
vowels = 0
consonants = 0

for ch in article.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Longest and Shortest Word
longest_word = words[0]
shortest_word = words[0]

for word in words:
    clean_word = word.strip(".,")
    
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

    if len(clean_word) < len(shortest_word):
        shortest_word = clean_word

# Word Frequency Dictionary
freq = {}

for word in words:
    word = word.strip(".,")
    
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Most Frequent Word
most_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        most_word = word

# Words Appearing Once
print("\nWORDS APPEARING ONLY ONCE:")
for word in freq:
    if freq[word] == 1:
        print(word)

# Words Appearing More Than 5 Times
print("\nWORDS APPEARING MORE THAN 5 TIMES:")
for word in freq:
    if freq[word] > 5:
        print(word)

# Count Words Starting With Each Alphabet
alphabet_count = {}

for word in freq:
    first = word[0]

    if first in alphabet_count:
        alphabet_count[first] += 1
    else:
        alphabet_count[first] = 1

print("\nWORDS STARTING WITH EACH ALPHABET:")
for letter in alphabet_count:
    print(letter, ":", alphabet_count[letter])

# Unique Words
print("\nUNIQUE WORDS:")
for word in freq:
    print(word)

# Average Word Length
total_length = 0

for word in words:
    total_length += len(word.strip(".,"))

average_word_length = total_length / total_words

# Vocabulary Size
vocabulary_size = len(freq)

# Final Summary
print("\n========== TEXT SUMMARY ==========")
print("Total Characters :", total_characters)
print("Total Words :", total_words)
print("Total Sentences :", total_sentences)
print("Vowels :", vowels)
print("Consonants :", consonants)
print("Longest Word :", longest_word)
print("Shortest Word :", shortest_word)
print("Most Frequent Word :", most_word)
print("Average Word Length :", round(average_word_length, 2))
print("Vocabulary Size :", vocabulary_size)