from utils import books

def addbook():
    book_name = input("Enter the book name which you want to add: ").strip().upper()
    books.append(book_name)
    print(f"The book {book_name} has been added to the library.")