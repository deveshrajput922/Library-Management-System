from utils import books, issued_books

def returnbook():
    book_name = input("Enter the name of the book you want to return :").strip().upper()
    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print("Thankyou ,you have returned the book successfully.")
    else:
        print("Sorry, the book is not issued from the library.")