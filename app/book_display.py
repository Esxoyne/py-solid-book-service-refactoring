from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(BookDisplay):

    def display(self, book: Book) -> None:
        print(book.get_content())


class ReverseDisplay(BookDisplay):

    def display(self, book: Book) -> None:
        print(book.get_content()[::-1])