
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(self.title, "has been borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(self.title, "has been returned.")


book1 = Book("Secret Seven", "Enid Blyton")
book2 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
book3 = Book("Harry Potter", "J.K. Rowling")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()
