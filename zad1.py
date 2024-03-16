class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


student_1 = Student("Patryk", [50, 60, 70])
student_2 = Student("Kajetan", [40, 30, 20])


print(student_1.is_passed())
print(student_2.is_passed())
