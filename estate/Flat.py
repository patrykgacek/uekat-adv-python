from estate.Property import Property


class Flat(Property):
    def __init__(
        self, area: int, rooms: int, price: int, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self) -> str:
        return f"{super().__str__()} {self.floor}"
