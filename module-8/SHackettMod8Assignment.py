import json

# Function to print student list
def print_class_list(student_list, notification):
    print(notification)
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']}: ID = {student['Student_ID']}, Email = {student['Email']}")
    print("\n")

# Had trouble with duplication so added function to prevent unwanted duplicates
def remove_duplicates(student_list):
    seen_ids = set()
    unique_students = []
    for student in student_list:
        if student['Student_ID'] not in seen_ids:
            unique_students.append(student)
            seen_ids.add(student['Student_ID'])
    return unique_students

# Load data from JSON file print message of students in list or error
file_path = "students.json"

try:
    with open(file_path, "r") as file:
        students = json.load(file)
        print(f"Loaded {len(students)} students from file.")
except FileNotFoundError:
    students = []
    print("students.json not found. Starting with an empty list.")

# Call function that prevents duplicates
students = remove_duplicates(students)

# Print the original student list
print_class_list(students, "Original Student list:")

# New student to add
new_student = {
    "F_Name": "Scott",
    "L_Name": "Hackett",
    "Student_ID": 45678,
    "Email": "schackett@my365.bellevue.edu"
}

# Check for duplicates by Student_ID
if not any(student['Student_ID'] == new_student['Student_ID'] for student in students):
    students.append(new_student)
    print("New student added to the list.")
else:
    print("Duplicate detected. No changes made.")

# Remove duplicates before saving
students = remove_duplicates(students)

# Print the updated student list
print_class_list(students, "Updated Student list:")

# Prompt the user for confirmation to save the file
save_changes = input("The students.json file has changed. Do you want to save the changes? (yes/no): ").strip().lower()

if save_changes == 'yes':

# I didn’t get a pop-up message to reload on computer so I added a section giving user the option to save over file.
# Save the updated list back to the file
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)
    print("Notification: The students.json file has been updated.")
else:
    print("Notification: Changes were not saved.") 