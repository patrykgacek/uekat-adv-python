from school.Library import Library
from school.Book import Book
from school.Employee import Employee
from school.Student import Student
from school.Order import Order
from estate.Flat import Flat
from estate.House import House


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

print(student_1.is_passed())
print(student_2.is_passed())

print(order_1)
print(order_2)

flat = Flat(50, 3, 200000, "Warszawa, ul. Marszałkowska 10", 3)
house = House(100, 5, 500000, "Kraków, ul. Krakowska 10", 200)

print(flat)
print(house)
