from student import Student
from student_manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search by ID")
        print("6. Search by Name")
        print("7. Filter by Course")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                course = input("Enter Course: ")
                marks = float(input("Enter Marks: "))

                if age <= 0:
                    raise ValueError("Age must be positive.")

                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100.")

                student = Student(
                    student_id,
                    name,
                    age,
                    course,
                    marks
                )

                manager.add_student(student)

            elif choice == "2":
                manager.display_students()

            elif choice == "3":
                student_id = input("Enter Student ID to update: ")
                manager.update_student(student_id)

            elif choice == "4":
                student_id = input("Enter Student ID to delete: ")
                manager.delete_student(student_id)

            elif choice == "5":
                student_id = input("Enter Student ID: ")
                student = manager.search_by_id(student_id)

                if student:
                    student.display()
                else:
                    print("Student not found.")

            elif choice == "6":
                name = input("Enter student name: ")
                manager.search_by_name(name)

            elif choice == "7":
                course = input("Enter course: ")
                manager.filter_by_course(course)

            elif choice == "8":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print("Error:", error)

        except Exception as error:
            print("Unexpected error:", error)


if __name__ == "__main__":
    main()