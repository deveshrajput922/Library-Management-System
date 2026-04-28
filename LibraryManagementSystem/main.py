from add_books import addbook
from show_books import showbooks
from return_books import returnbook
from issue_books import issuebook

def library():
    while True:
        print("Welcome to the Library , Please select an option to proceed :")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = (input("Enter your choice: "))
        if choice.isdigit():
            choice = int(choice)
            if choice == 1: 
                addbook()
            elif choice == 2: 
                showbooks()
            elif choice == 3:
                issuebook()
            elif choice == 4:
                returnbook()
            elif choice == 5:
                print("Thank you ")
                break
        else:
            print("Invalid choice. Please try again.")



library()
