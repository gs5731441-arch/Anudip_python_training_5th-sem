# Program to check whether a number is Prime or Not

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
        i += 1
    else:
        print(num, "is a Prime Number")