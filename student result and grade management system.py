# Student Result and Grade Management System

students = []


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# Add student
def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / 5

    if any(mark < 33 for mark in marks):
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"
        grade = calculate_grade(percentage)

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


# Display all students
def display_students():
    print("\n--- All Student Results ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n----------------------------")
        print("Roll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Marks       :", student["marks"])
        print("Total       :", student["total"], "/ 500")
        print("Percentage  :", round(student["percentage"], 2), "%")
        print("Grade       :", student["grade"])
        print("Result      :", student["result"])


# Search student
def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Marks      :", student["marks"])
            print("Total      :", student["total"], "/ 500")
            print("Percentage :", round(student["percentage"], 2), "%")
            print("Grade      :", student["grade"])
            print("Result     :", student["result"])
            return

    print("Student not found.")


# Main menu
while True:

    print("\n===================================")
    print(" STUDENT RESULT & GRADE MANAGEMENT")
    print("===================================")
    print("1. Add Student")
    print("2. Display All Results")
    print("3. Search Student")
    print("4. Exit")
    print("===================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")