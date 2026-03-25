# print("hello")
# choice = int(input("Enter your choice :"))
# print(choice)
from book import Book
from author import Author
from publisher import Publisher

python_book = Book(
                    title = "Python for FSD",
                    author = [Author("HP"),Author("Punit"),Author("Alex")],
                    publisher = Publisher("ITVEDANT"),
                    price = 123.22,
                    is_available = True,
                    edition = 1,
                    language = "English"
)
print(python_book)


class Library:
    books = []
    @classmethod
    def add_book(cls,book):
        cls.books.append(book)