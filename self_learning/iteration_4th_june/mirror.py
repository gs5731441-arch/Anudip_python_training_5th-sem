# Program to check whether a number is a Mirror Number

num = input("Enter a number: ")

length = len(num)

if length % 2 == 0:
    half = length // 2

    left = num[:half]
    right = num[half:]

    if left == right:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
else:
    print("Not a Mirror Number")