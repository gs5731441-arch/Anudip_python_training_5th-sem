# Program to check whether three sides form a triangle

a = float(input("Enter side a: "))

if a <= 0:
    print("Invalid side a!")
else:
    b = float(input("Enter side b: "))

    if b <= 0:
        print("Invalid side b!")
    else:
        c = float(input("Enter side c: "))

        if c <= 0:
            print("Invalid side c!")
        else:
            if (a + b > c) and (a + c > b) and (b + c > a):

                print("The sides form a Triangle.")

                if a == b == c:
                    print("Type: Equilateral Triangle")
                elif a == b or b == c or a == c:
                    print("Type: Isosceles Triangle")
                else:
                    print("Type: Scalene Triangle")

            else:
                print("The sides do NOT form a Triangle.")