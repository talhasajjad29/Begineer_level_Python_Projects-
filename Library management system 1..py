# Terminal Based Library System Using Class and Functions in Python(user can add, borrow, return, and view books.)
#  using instance and class methods,lists of dictionaries, conditionals, loops, user input, and string handling.

class Book:
    def __init__(self):
        self.books = []

    def __str__(self):
        return f"The list of books is: {self.books}"

    # Method to add books
    def add_books(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = {"title": title, "author": author, "status": "available"}
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    # Method to borrow a book
    def borrow_books(self):
        title = input("Enter the title of the book to borrow: ")
        for book in self.books:
            if book["title"].lower() == title.lower() and book["status"] == "available":
                book["status"] = "borrowed"
                print(f"You have borrowed '{title}'.")
                return
        print(f"The book '{title}' is not available for borrowing.")

    # Method to return a book
    def return_books(self):
        title = input("Enter the title of the book to return: ")
        for book in self.books:
            if book["title"].lower() == title.lower() and book["status"] == "borrowed":
                book["status"] = "available"
                print(f"You have returned '{title}'.")
                return
        print(f"Book '{title}' was not borrowed or doesn't exist. Please return manually.")

    # Method to check current books
    def current_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(f"Title: {book['title']}, Status: {book['status']}")
                print("-" * 30)

    # Main menu
    def main_menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Check Books")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_books()
            elif choice == "2":
                self.borrow_books()
            elif choice == "3":
                self.return_books()
            elif choice == "4":
                self.current_books()
            elif choice == "5":
                print("Exiting the Library System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create object and run the system
library = Book()
library.main_menu()
