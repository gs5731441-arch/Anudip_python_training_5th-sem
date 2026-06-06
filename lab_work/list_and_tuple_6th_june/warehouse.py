products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)
        fail_count += 1
    else:
        pass_count += 1

    # Stop if 3 failures found
    if fail_count == 3:
        print("3 failures found. Stopping inspection.")
        break

total_checked = pass_count + fail_count
pass_percentage = (pass_count / total_checked) * 100

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)
print("Pass Percentage:", pass_percentage, "%")