# transaction.py

from book import Book
from author import Author

class Transaction:
    def __init__(self, transaction_id, book, author, amount):
        self.transaction_id = transaction_id
        self.book = book
        self.author = author
        self.amount = amount

    def display_info(self):
        print(f"Transaction ID: {self.transaction_id}")
        self.book.display_info()
        self.author.display_info()
        print(f"Amount: ${self.amount}")
