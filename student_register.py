num_students = int(input("Enter the number of students to register: "))

with open('reg_form.txt', 'w') as file:
    for _ in range(num_students):
        student_id = input("Enter student ID number: ")
        file.write(student_id + '\n' + '-' * 20 + '\n')

print("Registration form created successfully.")