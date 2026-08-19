import json
from student import Student


class StudentManager:

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    # File Handling - Read
    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.students = [
                    Student.from_dict(student) for student in data
                ]
        except FileNotFoundError:
            self.students = []
        except json.JSONDecodeError:
            print("Error: Student file is corrupted.")
            self.students = []

    # File Handling - Write
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    # CREATE
    def add_student(self, student):
        if self.search_by_id(student.student_id):
            print("Student ID already exists.")
            return

        self.students.append(student)
        self.save_students()
        print("Student added successfully.")

    # READ
    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()

    # UPDATE
    def update_student(self, student_id):
        student = self.search_by_id(student_id)

        if not student:
            print("Student not found.")
            return

        try:
            student.name = input(
                f"Enter name [{student.name}]: "
            ) or student.name

            student.age = int(
                input(f"Enter age [{student.age}]: ")
                or student.age
            )

            student.course = input(
                f"Enter course [{student.course}]: "
            ) or student.course

            student.marks = float(
                input(f"Enter marks [{student.marks}]: ")
                or student.marks
            )

            self.save_students()
            print("Student updated successfully.")

        except ValueError:
            print("Invalid input. Update failed.")

    # DELETE
    def delete_student(self, student_id):
        student = self.search_by_id(student_id)

        if not student:
            print("Student not found.")
            return

        self.students.remove(student)
        self.save_students()
        print("Student deleted successfully.")

    # SEARCH
    def search_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_by_name(self, name):
        results = [
            student for student in self.students
            if name.lower() in student.name.lower()
        ]

        if results:
            for student in results:
                student.display()
        else:
            print("No students found.")

    # FILTER
    def filter_by_course(self, course):
        results = [
            student for student in self.students
            if student.course.lower() == course.lower()
        ]

        if results:
            for student in results:
                student.display()
        else:
            print("No students found for this course.")