# Student Performance Analytics System
"""
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary.
Example Structure students = {     
"S101": {"name": "Anuj", "marks": 85},     
"S102": {"name": "Rahul", "marks": 72} } 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
    o A (90+)  
    o B (75–89)  
    o C (50–74)  
    o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
    • Nested Dictionaries  
    • Dictionary Traversal  
    • Searching  
    • Aggregation  
    • Report Generation  
"""
# Student Performance Analytics System
# create and storer details of 30 students in dictionary
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Karan", "marks": 48},
    "S105": {"name": "Neha", "marks": 67},
    "S106": {"name": "Aman", "marks": 95},
    "S107": {"name": "Riya", "marks": 76},
    "S108": {"name": "Vikas", "marks": 59},
    "S109": {"name": "Pooja", "marks": 88},
    "S110": {"name": "Arjun", "marks": 45},
    "S111": {"name": "Simran", "marks": 80},
    "S112": {"name": "Rohit", "marks": 70},
    "S113": {"name": "Megha", "marks": 92},
    "S114": {"name": "Deepak", "marks": 54},
    "S115": {"name": "Sonia", "marks": 61},
    "S116": {"name": "Nikhil", "marks": 83},
    "S117": {"name": "Kavya", "marks": 97},
    "S118": {"name": "Mohit", "marks": 73},
    "S119": {"name": "Payal", "marks": 64},
    "S120": {"name": "Yash", "marks": 50},
    "S121": {"name": "Tina", "marks": 89},
    "S122": {"name": "Harsh", "marks": 46},
    "S123": {"name": "Sneha", "marks": 78},
    "S124": {"name": "Aditya", "marks": 68},
    "S125": {"name": "Isha", "marks": 93},
    "S126": {"name": "Manav", "marks": 57},
    "S127": {"name": "Naina", "marks": 82},
    "S128": {"name": "Varun", "marks": 41},
    "S129": {"name": "Khushi", "marks": 87},
    "S130": {"name": "Rajat", "marks": 74}
}
# 1. Display all student records
print("Student Records:")
for sid in students:
    print(sid, ":", students[sid])
# 2. Search a student using Student ID
search_id = input("\nEnter Student ID to search: ")
if search_id in students:
    print("Record Found:", students[search_id])
else:
    print("Student not found.")
# 3. Add a new student
new_id = input("\nEnter New Student ID: ")
new_name = input("Enter Student Name: ")
new_marks = int(input("Enter Marks: "))
students[new_id] = {"name": new_name, "marks": new_marks}
print("Student Added Successfully!")
# 4. Update marks of an existing student
update_id = input("\nEnter Student ID to update marks: ")
if update_id in students:
    marks = int(input("Enter New Marks: "))
    students[update_id]["marks"] = marks
    print("Marks Updated!")
else:
    print("Student not found.")
# 5. Delete a student
delete_id = input("\nEnter Student ID to delete: ")
if delete_id in students:
    del students[delete_id]
    print("Student Deleted!")
else:
    print("Student not found.")
# 6. Find topper and lowest scorer (without max/min)
first = True
for sid in students:
    if first:
        topper_id = sid
        lowest_id = sid
        first = False
    else:
        if students[sid]["marks"] > students[topper_id]["marks"]:
            topper_id = sid
        if students[sid]["marks"] < students[lowest_id]["marks"]:
            lowest_id = sid
print("\nTopper:", students[topper_id]["name"], "-", students[topper_id]["marks"])
print("Lowest Scorer:", students[lowest_id]["name"], "-", students[lowest_id]["marks"])
# 7. Calculate class average (without sum)
total = 0
count = 0
for sid in students:
    total = total + students[sid]["marks"]
    count = count + 1
average = total / count
print("Class Average:", average)
# 8. Count pass and fail students
pass_count = 0
fail_count = 0
for sid in students:
    if students[sid]["marks"] >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)
# 9. Generate Grades
print("\nStudent Grades:")
for sid in students:
    marks = students[sid]["marks"]
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
    print(sid, "-", students[sid]["name"], ":", grade)
# 10. Display students scoring above average
print("\nStudents Scoring Above Average:")
for sid in students:
    if students[sid]["marks"] > average:
        print(students[sid]["name"], "-", students[sid]["marks"])
# 11. Display Top 5 Performers
print("\nTop 5 Performers:")
temp = students.copy()
for i in range(5):
    first = True
    for sid in temp:
        if first:
            best_id = sid
            first = False
        elif temp[sid]["marks"] > temp[best_id]["marks"]:
            best_id = sid
    print(i + 1, ".", temp[best_id]["name"], "-", temp[best_id]["marks"])
    del temp[best_id]
# 12. Create separate dictionary for scholarship students
scholarship = {}
for sid in students:
    if students[sid]["marks"] > 85:
        scholarship[sid] = students[sid]
print("\nScholarship Students:")
for sid in scholarship:
    print(sid, ":", scholarship[sid])