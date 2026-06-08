contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# 1. Display all contact names in alphabetical order
print("Contact Names in Alphabetical Order:")

names = list(contacts.keys())
names.sort()

for name in names:
    print(name)

# 2. Count total number of contacts
count = 0

for name in contacts:
    count += 1

print("\nTotal Contacts =", count)

# 3. Search for a given contact name
search_name = input("\nEnter Contact Name to Search: ")

found = False

for name, number in contacts.items():

    if name.lower() == search_name.lower():      # Validation
        print("Contact Found")
        print("Name :", name)
        print("Number :", number)
        found = True
        break

if found == False:      # Validation
    print("Contact Not Found")

# 4. Create a list of contacts whose names start with a vowel
vowel_contacts = []

for name in contacts:

    if name[0].lower() in "aeiou":      # Validation
        vowel_contacts.append(name)

print("\nContacts Starting with a Vowel:")
print(vowel_contacts)

# 5. Search using break
search_name = input("\nEnter Contact Name to Search Again: ")

for name, number in contacts.items():

    if name.lower() == search_name.lower():      # Validation
        print("Contact Found:", name, "-", number)
        break