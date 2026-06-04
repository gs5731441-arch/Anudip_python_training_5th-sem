# Simple Interest with Separate Validation (Without Exception)
p = float(input("Enter Principal Amount: "))
if p <= 0:
    print("Invalid Principal Amount!")
else:
    r = float(input("Enter Rate of Interest: "))
    if r <= 0:
        print("Invalid Rate of Interest!")
    else:
        t = float(input("Enter Time (in years): "))
        if t <= 0:
            print("Invalid Time!")
        else:
            si = (p * r * t) / 100
            print("Simple Interest =", si)