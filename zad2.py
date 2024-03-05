class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hous: str, phone: str
    ):
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.open_hous: str = open_hous
        self.phone: str = phone

    def __str__(self) -> str:
        return (
            f"{self.city} {self.street} {self.zip_code} {self.open_hous} {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.hire_date: str = hire_date
        self.birth_date: str = birth_date
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.phone: str = phone

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.hire_date} {self.birth_date} {self.city} {self.street} {self.zip_code} {self.phone}"


class Book:
    def __init__(
        self,
        library: str,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: str,
    ):
        self.library: Library = library
        self.publication_date: str = publication_date
        self.author_name: str = author_name
        self.author_surname: str = author_surname
        self.number_of_pages: str = number_of_pages

    def __str__(self) -> str:
        return f"{self.library} {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}"


class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name: str = name
        self.marks: str = marks

    def __str__(self) -> str:
        return f"{self.name}"

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


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


lib_1 = Library("Warszawa", "Marszalkowska", "00-001", "8:00-16:00", "356-432-532")
lib_2 = Library("Krakow", "Krakowska", "00-002", "8:00-16:00", "643-279-461")
book_1 = Book(lib_1, "2021-01-01", "Jan", "Kowalski", 100)
book_2 = Book(lib_2, "2022-05-11", "Anna", "Nowak", 256)
book_3 = Book(lib_1, "2020-01-01", "Jan", "Kolonka", 345)
book_4 = Book(lib_2, "2021-04-12", "Krystian", "Wożniak", 534)
book_5 = Book(lib_1, "2021-08-27", "Krystyna", "Wokulska", 3256)
employee_1 = Employee(
    "Jan",
    "Nowak",
    "2021-01-01",
    "1990-01-01",
    "Warszawa",
    "Marszalkowska",
    "00-001",
    "468-234-122",
)
employee_2 = Employee(
    "Beata",
    "Opalony",
    "2021-06-10 ",
    "1990-05-30",
    "Krakow",
    "Krakowska",
    "00-002",
    "112-775-345",
)
employee_3 = Employee(
    "Krzysztof",
    "Kowalski",
    "2021-01-01",
    "1990-01-01",
    "Warszawa",
    "Marszalkowska",
    "00-001",
    "234-222-888",
)
student_1 = Student("Patryk", [50, 60, 70])
student_2 = Student("Kajetan", [40, 30, 20])
student_3 = Student("Grzegorz", [70, 20, 10])
order_1 = Order(employee_1, student_1, [book_1, book_2], "2024-01-01")
order_2 = Order(employee_2, student_2, [book_3, book_4, book_5], "2023-10-10")


print(order_1)
print(order_2)
