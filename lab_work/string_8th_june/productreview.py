review = "This product is excellent excellent excellent and very useful"

words = review.split()

# Validation: Review should not be empty
if len(review) > 0:

    # 1. Count Total Words
    total_words = len(words)
    print("Total Words:", total_words)

    # 2. Create Dictionary of Word Frequencies
    freq = {}

    for word in words:

        if word in freq:      # Validation
            freq[word] += 1

        else:
            freq[word] = 1

    print("\nWord Frequencies:")

    for word, count in freq.items():
        print(word, "->", count)

    # 3. Find Most Frequent Word
    first = True

    for word, count in freq.items():

        if first == True:
            max_word = word
            max_count = count
            first = False

        elif count > max_count:      # Validation
            max_word = word
            max_count = count

    print("\nMost Frequent Word:", max_word)

    # 4. Find Words Appearing Only Once
    once_words = []

    for word, count in freq.items():

        if count == 1:      # Validation
            once_words.append(word)

    print("Words Appearing Once:", once_words)

    # 5. Count Words Having More Than 5 Characters
    long_word_count = 0

    for word in words:

        if len(word) > 5:      # Validation
            long_word_count += 1

    print("Words Having More Than 5 Characters:", long_word_count)

    # 6. Display Words in Reverse Order
    print("\nWords in Reverse Order:")

    for i in range(len(words)-1, -1, -1):
        print(words[i], end=" ")

    # 7. Create List of Unique Words
    unique_words = []

    for word in words:

        if word not in unique_words:      # Validation
            unique_words.append(word)

    print("\n\nUnique Words:", unique_words)

else:
    print("Review is Empty")