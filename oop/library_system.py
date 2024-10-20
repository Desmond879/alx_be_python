# Base class - Book
class Book:
    def __init__(self, title, author):
        """Initialize the common attributes of all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book."""
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        """Initialize an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
