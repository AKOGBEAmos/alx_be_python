# Library system implementation with basic features:

class Book: 
    def __init__(self, title, author):
        self.title =  title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

""" Ebook class inherits from  Book """
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

""" PrintBook inherits from Book """
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count 
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
""" Library is a class that stores all the three categories of books """
class Library:
    def __init__(self, books = []):
        self.books = books

    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)