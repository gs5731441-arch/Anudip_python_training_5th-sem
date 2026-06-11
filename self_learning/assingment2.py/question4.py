# Vehicle Registration Verification System

vehicles = [
    "MH12AB4589",
    "MH14CD1234",
    "MH20EF5678",
    "MH01GH9876",
    "MH05IJ4321",
    "MH18KL1111",
    "DL05XY9988",
    "DL02AB1234",
    "DL08CD5678",
    "DL10EF4321",
    "KA03PQ1234",
    "KA05RS5678",
    "KA07TU1111",
    "KA09VW2222",
    "KA11XY3333",
    "UP32AB1234",
    "UP15CD5678",
    "UP20EF1111",
    "UP25GH2222",
    "UP30IJ3333"
]

mh = 0
dl = 0
ka = 0
up = 0

for reg in vehicles:

    print("\nRegistration Number :", reg)

    # Extract Parts
    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:6]
    vehicle_no = reg[6:10]

    print("State Code :", state)
    print("District Code :", district)
    print("Series :", series)
    print("Vehicle Number :", vehicle_no)

    # Count Letters and Digits
    letters = 0
    digits = 0

    for ch in reg:

        if ch.isalpha():
            letters += 1

        elif ch.isdigit():
            digits += 1

    print("Letters :", letters)
    print("Digits :", digits)

    # Validation
    valid = True

    if len(reg) != 10:
        valid = False

    elif not reg[0:2].isalpha():
        valid = False

    elif not reg[2:4].isdigit():
        valid = False

    elif not reg[4:6].isalpha():
        valid = False

    elif not reg[6:10].isdigit():
        valid = False

    if valid:
        print("Valid Registration")

        if state == "MH":
            mh += 1

        elif state == "DL":
            dl += 1

        elif state == "KA":
            ka += 1

        elif state == "UP":
            up += 1

    else:
        print("Invalid Registration")

# State Wise Report
print("\n========== STATE REPORT ==========")

print("MH ->", mh, "Vehicles")
print("DL ->", dl, "Vehicles")
print("KA ->", ka, "Vehicles")
print("UP ->", up, "Vehicles")