from estate.Property import Property


class House(Property):
    def __init__(
        self, area: int, rooms: int, price: int, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot: int = plot

    def __str__(self) -> str:
        return f"{super().__str__()} {self.plot}"
