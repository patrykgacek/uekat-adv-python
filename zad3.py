class Property:
    def __init__(
        self, area: int, rooms: int, price: int, address: str
    ) -> None:
        self.area: int = area
        self.rooms: int = rooms
        self.price: int = price
        self.address: str = address

    def __str__(self) -> str:
        return f"{self.area} {self.rooms} {self.price} {self.address}"


class House(Property):
    def __init__(
        self, area: int, rooms: int, price: int, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot: int = plot

    def __str__(self) -> str:
        return f"{super().__str__()} {self.plot}"


class Flat(Property):
    def __init__(
        self, area: int, rooms: int, price: int, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self) -> str:
        return f"{super().__str__()} {self.floor}"


flat = Flat(50, 3, 200000, "Warszawa, ul. Marszałkowska 10", 3)
house = House(100, 5, 500000, "Kraków, ul. Krakowska 10", 200)

print(flat)
print(house)
