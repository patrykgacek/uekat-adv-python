class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str) -> None:
        self.area: int = area
        self.rooms: int = rooms
        self.price: int = price
        self.address: str = address

    def __str__(self) -> str:
        return f"{self.area} {self.rooms} {self.price} {self.address}"
