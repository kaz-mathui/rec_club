class User:
    def __init__(self, id: int, details: str, account_type: int):
        """
        User constructor.
        """
        self.user_id = id
        self.details = details
        self.account_type = account_type


class Book:
    def __init__(self, id: int, details: str):
        """
        Book constructor.
        """
        self.book_id = id
        self.details = details


class Display:
    def __init__(self):
        """
        Display constructor.
        """
        self.active_book = None
        self.active_user = None
        self.page_number = 0

    def display_user(self, u: User):
        """
        Displays active user.
        """
        self.active_user = u
        self.refresh_username()

    def display_book(self, b: Book):
        """
        Displays active book.
        """
        self.active_book = b
        self.page_number = 0

        self.refresh_title()
        self.refresh_details()
        self.refresh_page()

    def turn_page_forward(self):
        """
        Turns page forward.
        """
        self.page_number += 1
        self.refresh_page()

    def turn_page_back(self):
        """
        Turns page backwards.
        """
        self.page_number -= 1
        self.refresh_page()

    def refresh_username(self):
        """
        Updates username display.
        """
        pass

    def refresh_title(self):
        """
        Updates title display.
        """
        pass

    def refresh_details(self):
        """
        Udpates details display.
        """
        pass

    def refresh_page(self):
        """
        Updates page display.
        """
        pass


class UserManager:
    def __init__(self):
        """
        User Manager constructor.
        """
        self.users = {}

    def add_user(self, id: int, details: str, account_type: int) -> User:
        """
        Adds user to UserManager.
        """
        if id in self.users:
            return None
        user = User(id, details, account_type)
        self.users[id] = user
        return user

    def find(self, id: int) -> User:
        """
        Finds a user.
        """
        return self.users[id]

    def remove(self, id: int) -> bool:
        """
        Removes a user.
        """
        if id not in self.users:
            return False
        del self.users[id]
        return True


class Library:
    def __init__(self):
        """
        Library constructor.
        """
        self.books = {}

    def add_book(self, id: int, details: str) -> Book:
        """
        Adds a book to library.
        """
        if id in self.books:
            return None
        book = Book(id, details)
        self.books[id] = book
        return book

    def find(self, id: int) -> Book:
        """
        Finds a book.
        """
        return self.books[id]

    def remove(self, id: int) -> bool:
        """
        Removes a book.
        """
        if id not in self.books:
            return False
        del self.books[id]
        return True


class OnlineReaderSystem:
    def __init__(self):
        """
        OnlineReaderSystem constructor.
        """
        self.library = Library()
        self.user_manager = UserManager()
        self.display = Display()
        self.active_book = None
        self.active_user = None
