# This code reads student data from a JSON string, prints the original list,
# adds a new student to the list, and writes the updated list back to a JSON file.

import json

# JSON data representing students
student_data = '''
{
    "student": [
        
        {
            "F_Name": "Ellen",
            "L_Name": "Ripley",
            "Student_ID": 45604,
            "Email": "eripley@gmail.com"
        },
        {
            "F_Name": "Arthur",
            "L_Name": "Dallas",
            "Student_ID": 45605,
            "Email": "adallas@gmail.com"
        },
        {
            "F_Name": "Joan",
            "L_Name": "Lambert",
            "Student_ID": 45714,
            "Email": "jlambert@gmail.com"
        },
        {
            "F_Name": "Thomas",
            "L_Name": "Kane",
            "Student_ID": 68554,
            "Email": "tkane@gmail.com"
        }
           
    ]
}
'''
data = json.loads(student_data)

# Print the original student list
for student in data['student']:
    print(f"{student['L_Name']}, {student['F_Name']}: "
          f"ID = {student['Student_ID']}, Email = {student['Email']}")
    
print("This is the original Student list.")
print()

# Add a new student to the list
new_student = {
    "F_Name": "James",
    "L_Name": "Brown",
    "Student_ID": 13579,
    "Email": "jcb3@gmail.com"
}

# Append the new student to the existing list
data['student'].append(new_student)

with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)

print("This is the updated Student list.")

# Print the updated student list
for student in data['student']:
    print(f"{student['L_Name']}, {student['F_Name']}: "
          f"ID = {student['Student_ID']}, Email = {student['Email']}")  

print()
print("The json file was updated.")






