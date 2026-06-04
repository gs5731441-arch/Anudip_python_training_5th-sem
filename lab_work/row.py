# Accept the number of rows

rows = int(input("Enter number of rows: "))

# Pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()