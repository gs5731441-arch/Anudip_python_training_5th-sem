text = "AAABBBCCCDDDAAA"

print("Original Text:", text)

# Validation: Text should not be empty
if len(text) > 0:

    # 1 & 2. Character Frequencies Dictionary
    freq = {}

    for ch in text:

        if ch in freq:      # Validation
            freq[ch] += 1

        else:
            freq[ch] = 1

    print("\nCharacter Frequencies:")

    for ch, count in freq.items():
        print(ch, "->", count)

    # 3. Unique Characters
    unique_chars = []

    for ch in text:

        if ch not in unique_chars:      # Validation
            unique_chars.append(ch)

    print("\nUnique Characters:", unique_chars)

    # 4. Most Frequent Character
    first = True

    for ch, count in freq.items():

        if first == True:
            max_char = ch
            max_count = count
            first = False

        elif count > max_count:      # Validation
            max_char = ch
            max_count = count

    print("\nMost Frequent Character:", max_char)

    # 5. Create Compressed Output
    compressed = ""
    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i-1]:      # Validation
            count += 1

        else:
            compressed += text[i-1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

    print("Compressed Output:", compressed)

    # 6. Compression Ratio
    original_length = len(text)
    compressed_length = len(compressed)

    ratio = (compressed_length / original_length) * 100

    print("\nOriginal Length:", original_length)
    print("Compressed Length:", compressed_length)
    print("Compression Ratio:", round(ratio, 2), "%")

else:
    print("Text is Empty")