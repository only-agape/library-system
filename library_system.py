# library_system.py

from book import Book
from author import Author
from transaction import Transaction

# Create books
book1 = Book(1, "The Catcher in the Rye", "J.D. Salinger", 25.0)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 30.0)

# Create authors
author1 = Author(101, "Alice", "alice@example.com")
author2 = Author(102, "Bob", "bob@example.com")

# Create transactions
transaction1 = Transaction(1001, book1, author1, 2)
transaction2 = Transaction(1002, book2, author2, 1)

# Display information
print("Transaction Information:")
transaction1.display_info()
print()
transaction2.display_info()
