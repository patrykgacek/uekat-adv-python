class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name: str = name
        self.marks: str = marks

    def __str__(self) -> str:
        return f"{self.name}"

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50
