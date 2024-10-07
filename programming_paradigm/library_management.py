# library_management.py

class Book:
    """A class representing a book with title, author, and its availability status."""

    def __init__(self, title, author):
        """Initialize a new book with a title and author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track book's availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned and available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class to manage a collection of books in the library."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # Private attribute to hold the collection of books

    def add_book(self, book):
        """Add a new book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available in the library."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Successfully checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title if it is checked out."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Successfully returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books in the library at the moment.")
