# Program to check whether a number is prime or not
# If not prime, display all its factors

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")
        print("Factors are:")

        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")