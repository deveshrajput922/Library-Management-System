from utils import books

def showbooks():
    if len(books) == 0:
        print("Sorry, the books are not available in the library.")
    else:
        for i in books:
            print(">", i)