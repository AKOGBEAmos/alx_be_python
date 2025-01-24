# Library management module
class Book:
    def __init__(self,title, author, is_checked_out=0):
        self.title =  title
        self.author = author
        self.__is_checked_out = is_checked_out

    def is_checked_out(self):
        return self.__is_checked_out
    
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def book_checking(self,status):
        """ This method update the availability status of a book """
        self.__is_checked_out = bool(status)

class Library:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        """ Method to add a new Book to the library """
        self.__books.append(book)

    def check_out_book(self,title):
        #If a book is checked_out we make it unavailable in the library
        for book in self.__books:
            if title == book.title:
                book.book_checking(1)
        
    def return_book(self,title):
        #If a book is returned we make it available again
        for book in self.__books:
            if title == book.title and book.is_checked_out():
                book.book_checking(0)

    def list_available_books(self):
        for book in self.__books:
            if not book.is_checked_out():  
                print(f"{book.get_title()} by {book.get_author()}")
