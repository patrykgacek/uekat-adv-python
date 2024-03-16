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
