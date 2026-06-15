
import json
students = []
def add_stud():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    student = {"Name" : name, "Marks": marks}
    students.append(student)
    save_students()
    print("Student added successfully!!")
    
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)
def load_students():
    global students

    with open("students.json", "r") as file:
        students = json.load(file)
def search_stud():
    srch = input("Enter name of the student: ")
    found = False
    for student in students:
        if srch == student["Name"]:
            print("Student found!")
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])

            found = True
            break
    if not found:
        print("Student not found!!")
def del_stud():
    dele = input("Enter name of the student to delete data: ")
    for student in students:
        if dele == student["Name"]:
            students.remove(student)
            print("Deleted Successfully!!")
        else:
            print("Enter a valid name!!")
    save_students()
load_students()
while True:
    print("STUDENT RESULT MANAGER")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search student")
    print("4. Delete Student")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_stud()

    elif choice == 2:
        print("\nStudent List:\n")
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                print()

    elif choice == 3:
        search_stud()   

    elif choice == 4:
        del_stud()

    elif choice == 5:
        print("Exited successfully!")
        break
    else:
        print("Inavlid Choice")