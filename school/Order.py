from school.Employee import Employee
from school.Student import Student
from school.Book import Book


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date: str
    ):
        self.employee: Employee = employee
        self.student: Student = student
        self.books: list[Book] = books
        self.order_date: str = order_date

    def __str__(self) -> str:
        return f"{self.employee} {self.student} {[str(x) for x in self.books]} {self.order_date}"
