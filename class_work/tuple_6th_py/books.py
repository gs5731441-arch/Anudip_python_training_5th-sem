books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Lists
unavailable_books = []
more_than_2_copies = []

# Count available books
available_count = 0

# Traverse records
for title, copies in books:

    # Unavailable books
    if copies == 0:
        unavailable_books.append(title)

    # Books with more than 2 copies
    if copies > 2:
        more_than_2_copies.append(title)

    # Available books count
    if copies > 0:
        available_count += 1

print("Unavailable Books:", unavailable_books)
print("Books with More Than 2 Copies:", more_than_2_copies)
print("Available Books Count:", available_count)

# Search a requested book
search_book = input("Enter book name to search: ")

for title, copies in books:
    if title.lower() == search_book.lower():
        print("Book Found!")
        print("Title:", title)
        print("Copies:", copies)
        break
else:
    print("Book Not Found!")