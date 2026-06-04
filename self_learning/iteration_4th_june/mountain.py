# Program to check whether a number is a Mountain Number

num = input("Enter a number: ")

peak = num.index(max(num))

# Peak should not be first or last digit
if peak == 0 or peak == len(num) - 1:
    print("Not a Mountain Number")
else:
    flag = True

    # Increasing part
    for i in range(peak):
        if num[i] >= num[i + 1]:
            flag = False
            break

    # Decreasing part
    if flag:
        for i in range(peak, len(num) - 1):
            if num[i] <= num[i + 1]:
                flag = False
                break

    if flag:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")