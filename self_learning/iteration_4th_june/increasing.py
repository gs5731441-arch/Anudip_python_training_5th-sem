# Program to find the length of the longest continuous increasing sequence

n = int(input("Enter number of elements: "))

max_len = 1
current_len = 1

prev = int(input("Enter number 1: "))

for i in range(2, n + 1):
    num = int(input("Enter number " + str(i) + ": "))

    if num > prev:
        current_len += 1
    else:
        current_len = 1

    if current_len > max_len:
        max_len = current_len

    prev = num

print("Longest Sequence Length =", max_len)