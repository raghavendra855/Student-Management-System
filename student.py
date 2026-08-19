class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["marks"]
        )

    def display(self):
        print(
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Course: {self.course} | "
            f"Marks: {self.marks}"
        )