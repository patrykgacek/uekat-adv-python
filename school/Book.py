from school.Library import Library


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
