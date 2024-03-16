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
