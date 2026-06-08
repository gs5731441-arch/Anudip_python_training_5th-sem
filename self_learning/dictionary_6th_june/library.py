books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# 1. Display books that are currently unavailable
print("Unavailable Books:")

for book, copies in books.items():

    if copies == 0:      # Validation
        print(book)

# 2. Count the number of available books
available_count = 0

for copies in books.values():

    if copies > 0:      # Validation
        available_count += 1

print("\nNumber of Available Books =", available_count)

# 3. Find the book with maximum copies
first = True

for book, copies in books.items():

    if first == True:
        max_book = book
        max_copies = copies
        first = False

    elif copies > max_copies:      # Validation
        max_copies = copies
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, ":", max_copies)

# 4. Create a list of books having less than 3 copies
low_stock_books = []

for book, copies in books.items():

    if copies < 3:      # Validation
        low_stock_books.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(low_stock_books)

# 5. Calculate total number of books available
total_books = 0

for copies in books.values():

    if copies >= 0:      # Validation
        total_books += copies

print("\nTotal Number of Books Available =", total_books)