from utils import issued_books, books

def issuebook():
    book_name = input("Enter the name of the book you want to issue :").strip().upper()
    if book_name in books:
        books.remove(book_name)
        issued_books.append(book_name)
        print("you have issued the book successfully.")
    else:
        print("Sorry, the book is not available in the library.")
