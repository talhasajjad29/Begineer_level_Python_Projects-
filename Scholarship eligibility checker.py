# Filters students eligible for scholarships based on GPA and graduation status,and allows lookup by roll number.
# use Nested Lists • Data Filtering (Loops & Conditions) • Input & Type Conversion
# # • Error Handling (try‑except) • Search Operations in Lists • Boolean Logic

student_data = [
    [1, "Talha", 3.4, True], [2, "Ahad", 3.1, False],
    [3, "Samad", 3.8, True], [4, "Ahmad", 3.5, True],
    [5, "Zubair", 3.3, False], [6, "Zuhaib", 3.8, True],
    [7, "Abdul", 3.7, False], [8, "Faizan", 3.9, True],
    [9, "Wahab", 3.2, False], [10, "Ali", 3.7, False]
]

scholarship = []

# Step 1: Filter eligible students (GPA >= 3.5 and graduated)
for student in student_data:
    if student[2] >= 3.5 and student[3] == True:
        scholarship.append([student[0], student[1]])

# Step 2: Show eligible students
print(" Scholarship Eligible Students:")
for s in scholarship:
    print(f"Roll No: {s[0]}, Name: {s[1]}")
print("------------------------------------------------------")

# Step 3: Check if a particular student is eligible
try:
    user_rollno = int(input("Enter roll number to check scholarship eligibility: "))
    found = False

    for s in scholarship:
        if s[0] == user_rollno:
            print(f" Student Found: Roll No: {s[0]}, Name: {s[1]}")
            found = True
            break

    if not found:
        print(" Student is not eligible for scholarship.")
except ValueError:
    print(" Please enter a valid numeric roll number.")
