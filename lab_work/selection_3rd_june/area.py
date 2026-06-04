# Program to calculate Area and Perimeter of a Rectangle

length = float(input("Enter Length: "))

if length <= 0:
    print("Invalid Length!")
else:
    breadth = float(input("Enter Breadth: "))

    if breadth <= 0:
        print("Invalid Breadth!")
    else:
        area = length * breadth
        perimeter = 2 * (length + breadth)

        print("Area of Rectangle =", area)
        print("Perimeter of Rectangle =", perimeter)