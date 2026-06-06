
#kutubxona  tizmi.

from datetime import datetime

# ---------------- Book ----------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_info(self):
        return f"{self.title} - {self.author}"

    def is_available(self):
        return self.available

# ---------------- Student ----------------
class Student:
    def __init__(self, name):
        self.name = name
        self.books = []

    def get_fullname(self):
        return self.name

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.books.append(book)
            print(self.name, "oldi:", book.title)

    def return_book(self, book):
        if book in self.books:
            book.available = True
            self.books.remove(book)
            print(self.name, "qaytardi:", book.title)

    def get_borrowed_books(self):
        return [b.title for b in self.books]


# ---------------- Teacher ----------------
class Teacher:
    def __init__(self, name):
        self.name = name
        self.books = []

    def get_fullname(self):
        return self.name

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.books.append(book)
            print("Teacher", self.name, "oldi:", book.title)

    def return_book(self, book):
        if book in self.books:
            book.available = True
            self.books.remove(book)

    def get_info(self):
        return f"Teacher: {self.name}"

# ---------------- Library ----------------
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_available_books(self):
        print("\nMavjud kitoblar:")
        for b in self.books:
            if b.available:
                print(b.get_info())

    def show_all_users(self):
        print("\nFoydalanuvchilar:")
        for u in self.users:
            print(u.get_fullname())


# ---------------- BorrowRecord ----------------
class BorrowRecord:
    def __init__(self, book, user):
        self.book = book
        self.user = user
        self.date = datetime.now()

    def get_book_name(self):
        return self.book.get_title()

    def get_borrower_name(self):
        return self.user.get_fullname()

    def get_borrow_date(self):
        return self.date

    def get_info(self):
        return f"{self.get_borrower_name()} oldi {self.get_book_name()}"


# ---------------- TEST ----------------
b3 = Book("Math", "Karimov")
b1 = Book("Python", "Ali")
b2 = Book("AI", "Vali")

s1 = Student("Bexruzbek")
t1 = Teacher("Karimov")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.add_user(s1)
lib.add_user(t1)

# natijalar
lib.show_available_books()
s1.borrow_book(b1)

record = BorrowRecord(b1, s1)
print(record.get_info())

lib.show_available_books()
print("Student kitoblari:", s1.get_borrowed_books())
print(t1.get_info())




















from datetime import datetime

# ---------------- Person ----------------
class Person:
    def __init__(self, fullname, id, birth_year):
        self.fullname = fullname
        self.id = id
        self.birth_year = birth_year

    def get_fullname(self):
        return self.fullname

    def get_ID(self):
        return self.id

    def get_info(self):
        return f"{self.fullname} ({self.id})"

    def get_age(self, current_year):
        return current_year - self.birth_year
# ---------------- BankAccount ----------------
class BankAccount:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def check_balance(self):
        return self.balance

    def get_account_info(self):
        return f"Hisob: {self.number}, Balans: {self.balance}"
# ---------------- Client ----------------
class Client(Person):
    def __init__(self, fullname, id, birth_year):
        super().__init__(fullname, id, birth_year)  # ota klasni ishlatish uchun "super"
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        for acc in self.accounts:
            print(acc.get_account_info())

    def get_client_info(self):
        return self.get_info()

    def transfer_money(self, from_acc, to_acc, amount):
        if from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print("Pul o‘tkazildi")
# ---------------- Transaction ----------------
class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type
        self.date = datetime.now()

    def get_amount(self):
        return self.amount

    def get_type(self):
        return self.type

    def get_date(self):
        return self.date

    def get_info(self):
        return f"{self.type}: {self.amount} ({self.date})"
# ---------------- Bank ----------------
class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def show_clients(self):
        for c in self.clients:
            print(c.get_fullname())

    def find_account(self, account_number):
        for c in self.clients:
            for acc in c.accounts:
                if acc.number == account_number:
                    return acc

    def get_bank_info(self):
        return f"Bank: {self.name}, Clientlar: {len(self.clients)}"
    










from datetime import datetime
# 1. Room klassi
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.available = True

    def get_room_number(self):
        return self.room_number

    def is_available(self):
        return self.available

    def book_room(self):
        self.available = False

    def get_info(self):
        if self.available:
            holat = "Bo'sh"
        else:
            holat = "Band"
        return f"Xona raqami: {self.room_number}, Holati: {holat}"
# 2. Guest klassi
class Guest:
    def __init__(self, fullname):
        self.fullname = fullname
        self.reservation = None

    def get_fullname(self):
        return self.fullname

    def make_reservation(self, reservation):
        self.reservation = reservation

    def cancel_reservation(self):
        self.reservation = None

    def get_info(self):
        return f"Mehmon: {self.fullname}"
# 3. Reservation klassi
class Reservation:
    def __init__(self, room, check_in, check_out):
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def get_check_in(self):
        return self.check_in

    def get_check_out(self):
        return self.check_out

    def calculate_days(self):
        sana1 = datetime.strptime(self.check_in, "%Y-%m-%d")
        sana2 = datetime.strptime(self.check_out, "%Y-%m-%d")
        return (sana2 - sana1).days

    def get_info(self):
        return f"Xona: {self.room.room_number}, Kirish: {self.check_in}, Chiqish: {self.check_out}"
# 4. Payment klassi
class Payment:
    def __init__(self):
        self.status = "To'lanmagan"

    def make_payment(self, amount):
        self.status = "To'langan"

    def get_status(self):
        return self.status

    def get_info(self):
        return f"To'lov holati: {self.status}"

    def cancel_payment(self):
        self.status = "Bekor qilingan"
# 5. Hotel klassi
class Hotel:
    def __init__(self, name):
        
        self.name = name
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available_rooms(self):
        print("Bo'sh xonalar:")
        for room in self.rooms:
            if room.is_available():
                print(room.get_info())

    def add_guest(self, guest):
        self.guests.append(guest)

    def show_all_guests(self):
        print("Barcha mehmonlar:")
        for guest in self.guests:
            print(guest.get_info())
# ------------------ OBYEKTLAR ------------------
hotel = Hotel("Grand Hotel")

room1 = Room(101)
room2 = Room(102)

guest1 = Guest("Ali")
guest2 = Guest("Vali")

hotel.add_room(room1)
hotel.add_room(room2)

hotel.add_guest(guest1)
hotel.add_guest(guest2)

reservation1 = Reservation(room1, "2026-04-10", "2026-04-15")
guest1.make_reservation(reservation1)
room1.book_room()

payment1 = Payment()
payment1.make_payment(500000)
# ------------------ NATIJALAR ------------------
hotel.show_available_rooms()
print(guest1.get_info())
print(reservation1.get_info())
print(payment1.get_info())
