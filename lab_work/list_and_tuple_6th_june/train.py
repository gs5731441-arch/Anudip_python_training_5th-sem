passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Display waiting-list passengers
print("Waiting List Passengers:")
for name, status in passengers:
    if status == "Waiting":
        print(name)

# Count confirmed and waiting passengers
confirmed_count = 0
waiting_count = 0

for name, status in passengers:
    if status == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Check whether a passenger has a confirmed ticket
search_name = input("\nEnter passenger name: ")

found = False

for name, status in passengers:
    if name == search_name and status == "Confirmed":
        found = True
        break

if found:
    print(search_name, "has a Confirmed ticket")
else:
    print(search_name, "does not have a Confirmed ticket")

# Create separate lists
confirmed_list = []
waiting_list = []

for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    else:
        waiting_list.append(name)

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)