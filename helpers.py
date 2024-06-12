from books import Book
from students import Student
from librarians import Librarian
from borrowed_records import BorrowRecord
from datetime import date

# class Student:
#     student_db = []

def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.borrowed_books = []
        self.reserved_books = []
        self.is_blocked = False

def add_student(self):
        Student.student_db.append(self)

def remove_student(self):
        Student.student_db = [student for student in Student.student_db if student.student_id != self.student_id]

def update_student(self, name=None, grade=None):
    if name:
        self.name = name
    if grade:
        self.grade = grade

@classmethod
def find_student_by_id(cls, student_id):
    return next((student for student in cls.student_db if student.student_id == student_id), None)

@classmethod
def list_students(cls):
    return cls.student_db

def list_borrowed_books(self):
    return self.borrowed_books

def student_details(self):
    return {
        "student_id": self.student_id,
        "name": self.name,
        "grade": self.grade,
        "borrowed_books": self.borrowed_books,
        "reserved_books": self.reserved_books,
        "is_blocked": self.is_blocked
    }

@classmethod
def list_borrowed_books_by_id(cls, student_id):
    student = cls.find_student_by_id(student_id)
    return student.borrowed_books if student else None

@classmethod
def check_overdue_books_by_id(cls, student_id):
    student = cls.find_student_by_id(student_id)
    if student:
        overdue_books = [book for book in student.borrowed_books if book['due_date'] < date.today()]
        return overdue_books
    return None

def register_borrowed_books(self, books):
    self.borrowed_books.extend(books)

def register_returned_books(self, books):
    self.borrowed_books = [book for book in self.borrowed_books if book not in books]

def cancel_book_reservation(self, book_id):
    self.reserved_books = [book for book in self.reserved_books if book['book_id'] != book_id]

@classmethod
def list_reserved_books_by_id(cls, student_id):
    student = cls.find_student_by_id(student_id)
    return student.reserved_books if student else None

def send_reminders(self):
    overdue_books = [book for book in self.borrowed_books if book['due_date'] < date.today()]
    for book in overdue_books:
        print(f"Reminder: Book ID {book['book_id']} is overdue. Please return it as soon as possible.")

def block_student(self):
    self.is_blocked = True

def unblock_student(self):
    self.is_blocked = False

def check_blocked_status(self):
    return 'Blocked' if self.is_blocked else 'Unblocked'

@classmethod
def total_students(cls):
    return len(cls.student_db)

@classmethod
def total_overdue_students(cls):
    today = date.today()
    return len([student for student in cls.student_db if any(book['due_date'] < today for book in student.borrowed_books)])

# Example usage
# if __name__ == "__main__":
#     student1 = Student(1, "Alice", "10th")
#     student2 = Student(2, "Bob", "12th")

#     student1.add_student()
#     student2.add_student()

#     print(Student.list_students())
#     student1.register_borrowed_books([{"book_id": 101, "due_date": date(2024, 6, 10)}])
#     student2.register_borrowed_books([{"book_id": 102, "due_date": date(2024, 6, 5)}])

#     print(student1.list_borrowed_books())
#     print(student1.student_details())
#     print(Student.total_students())

#     print(Student.list_borrowed_books_by_id(1))
#     print(Student.check_overdue_books_by_id(2))

#     student2.register_returned_books([{"book_id": 102, "due_date": date(2024, 6, 5)}])
#     print(student2.list_borrowed_books())

#     student1.cancel_book_reservation(101)
#     student1.send_reminders()

#     student1.block_student()
#     print(student1.check_blocked_status())
#     student1.unblock_student()
#     print(student1.check_blocked_status())

#     print(Student.total_overdue_students())

# class Book:
#     library_db = []

def __init__(self, book_id, title, author, genre, year):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.genre = genre
    self.year = year
    self.is_borrowed = False
    self.is_reserved = False

def add_book(self):
    Book.library_db.append(self)

def remove_book(self):
    Book.library_db = [book for book in Book.library_db if book.book_id != self.book_id]

def update_book(self, title=None, author=None, genre=None, year=None):
    if title:
        self.title = title
    if author:
        self.author = author
    if genre:
        self.genre = genre
    if year:
        self.year = year

@classmethod
def find_book_by_title(cls, title):
    return [book for book in cls.library_db if book.title.lower() == title.lower()]

@classmethod
def find_book_by_author(cls, author):
    return [book for book in cls.library_db if book.author.lower() == author.lower()]

@classmethod
def list_books(cls):
    return cls.library_db

@classmethod
def list_available_books(cls):
    return [book for book in cls.library_db if not book.is_borrowed]

@classmethod
def list_borrowed_books(cls):
    return [book for book in cls.library_db if book.is_borrowed]

@classmethod
def check_availability(cls, book_id):
    book = next((book for book in cls.library_db if book.book_id == book_id), None)
    return book is not None and not book.is_borrowed

def mark_as_borrowed(self):
    if not self.is_borrowed:
        self.is_borrowed = True
        self.is_reserved = False

def mark_as_returned(self):
    if self.is_borrowed:
        self.is_borrowed = False

def get_book_details(self):
    return {
        "book_id": self.book_id,
        "title": self.title,
        "author": self.author,
        "genre": self.genre,
        "year": self.year,
        "is_borrowed": self.is_borrowed,
        "is_reserved": self.is_reserved
    }

@classmethod
def list_books_by_genre(cls, genre):
    return [book for book in cls.library_db if book.genre.lower() == genre.lower()]

@classmethod
def list_books_by_publication_year(cls, year):
    return [book for book in cls.library_db if book.year == year]

def reserve_book(self):
    if not self.is_borrowed and not self.is_reserved:
        self.is_reserved = True

def cancel_reservation(self):
    if self.is_reserved:
        self.is_reserved = False

@classmethod
def list_reserved_books(cls):
    return [book for book in cls.library_db if book.is_reserved]

@classmethod
def count_books(cls):
    return len(cls.library_db)

@classmethod
def count_available_books(cls):
    return len(cls.list_available_books())

@classmethod
def count_borrowed_books(cls):
    return len(cls.list_borrowed_books())


# Example usage
# if __name__ == "__main__":
#     book1 = Book(1, "Title1", "Author1", "Genre1", 2020)
#     book2 = Book(2, "Title2", "Author2", "Genre2", 2021)
    
#     book1.add_book()
#     book2.add_book()
    
#     print(Book.list_books())
#     print(Book.find_book_by_title("Title1"))
#     print(Book.find_book_by_author("Author2"))
#     print(Book.list_available_books())
    
#     book1.mark_as_borrowed()
#     print(Book.list_borrowed_books())
#     print(Book.check_availability(1))
    
#     book1.mark_as_returned()
#     print(Book.check_availability(1))
    
#     book1.reserve_book()
#     print(Book.list_reserved_books())
    
#     book1.cancel_reservation()
#     print(Book.list_reserved_books())
    
#     print(Book.count_books())
#     print(Book.count_available_books())
#     print(Book.count_borrowed_books())

# from datetime import date, timedelta

# class BorrowRecord:
#     borrow_db = []

def __init__(self, record_id, book_id, student_id, borrow_date, due_date):
    self.record_id = record_id
    self.book_id = book_id
    self.student_id = student_id
    self.borrow_date = borrow_date
    self.due_date = due_date
    self.return_date = None
    self.is_returned = False

def add_borrow_record(self):
    BorrowRecord.borrow_db.append(self)

def remove_borrow_record(self):
    BorrowRecord.borrow_db = [record for record in BorrowRecord.borrow_db if record.record_id != self.record_id]

def update_borrow_record(self, return_date=None, is_returned=None):
    if return_date:
        self.return_date = return_date
    if is_returned is not None:
        self.is_returned = is_returned

@classmethod
def search_borrow_record_by_book(cls, book_id):
    return [record for record in cls.borrow_db if record.book_id == book_id]

@classmethod
def search_borrow_record_by_student(cls, student_id):
    return [record for record in cls.borrow_db if record.student_id == student_id]

@classmethod
def list_borrow_records(cls):
    return cls.borrow_db

@classmethod
def list_borrow_records_by_id(cls, record_id):
    return [record for record in cls.borrow_db if record.record_id == record_id]

@classmethod
def list_borrow_records_by_book(cls, book_id):
    return cls.search_borrow_record_by_book(book_id)

def borrow_status(self):
    return "Returned" if self.is_returned else "Not Returned"

def return_status(self):
    return "Overdue" if self.return_date and self.return_date > self.due_date else "On Time"

@classmethod
def total_borrowed_books(cls):
    return len(cls.borrow_db)

@classmethod
def total_borrowed_books_by_id(cls, student_id):
    return len(cls.search_borrow_record_by_student(student_id))

@classmethod
def total_overdue_books(cls):
    today = date.today()
    return len([record for record in cls.borrow_db if not record.is_returned and record.due_date < today])

@classmethod
def total_overdue_books_by_id(cls, student_id):
    today = date.today()
    return len([record for record in cls.search_borrow_record_by_student(student_id) if not record.is_returned and record.due_date < today])

def send_notification(self):
    if not self.is_returned and self.due_date < date.today():
        # Simulate sending a notification
        print(f"Notification: Book ID {self.book_id} borrowed by Student ID {self.student_id} is overdue.")

def calculate_fine(self):
    if not self.is_returned and self.due_date < date.today():
        overdue_days = (date.today() - self.due_date).days
        fine_per_day = 1  # Example fine amount per day
        return overdue_days * fine_per_day
    return 0

@classmethod
def calculate_fine_by_id(cls, student_id):
    total_fine = 0
    for record in cls.search_borrow_record_by_student(student_id):
        total_fine += record.calculate_fine()
    return total_fine

def get_borrowed_book_details(self):
    return {
        "record_id": self.record_id,
        "book_id": self.book_id,
        "student_id": self.student_id,
        "borrow_date": self.borrow_date,
        "due_date": self.due_date,
        "return_date": self.return_date,
        "is_returned": self.is_returned
    }

@classmethod
def get_borrowed_book_details_by_id(cls, record_id):
    record = next((record for record in cls.borrow_db if record.record_id == record_id), None)
    return record.get_borrowed_book_details() if record else None

# Example usage
# if __name__ == "__main__":
#     borrow1 = BorrowRecord(1, 101, 1001, date(2024, 6, 1), date(2024, 6, 15))
#     borrow2 = BorrowRecord(2, 102, 1002, date(2024, 6, 5), date(2024, 6, 19))

#     borrow1.add_borrow_record()
#     borrow2.add_borrow_record()

#     print(BorrowRecord.list_borrow_records())
#     print(BorrowRecord.search_borrow_record_by_book(101))
#     print(BorrowRecord.search_borrow_record_by_student(1001))
#     print(BorrowRecord.total_borrowed_books())
#     print(BorrowRecord.total_borrowed_books_by_id(1001))
#     print(BorrowRecord.total_overdue_books())

#     borrow1.update_borrow_record(return_date=date(2024, 6, 16), is_returned=True)
#     print(borrow1.return_status())
#     print(borrow1.calculate_fine())
#     print(BorrowRecord.calculate_fine_by_id(1001))
#     print(borrow1.get_borrowed_book_details())

# class Librarian:
#     librarian_db = []
#     task_db = []

def __init__(self, librarian_id, name):
    self.librarian_id = librarian_id
    self.name = name
    self.tasks = []
    self.is_active = True
    self.is_blocked = False

def add_librarian(self):
    Librarian.librarian_db.append(self)

def authenticate_librarian(self):
    return next((librarian for librarian in Librarian.librarian_db if librarian.librarian_id == self.librarian_id and not librarian.is_blocked), None) is not None

def remove_librarian(self):
    Librarian.librarian_db = [librarian for librarian in Librarian.librarian_db if librarian.librarian_id != self.librarian_id]

def update_librarian(self, name=None):
    if name:
        self.name = name

@classmethod
def search_librarian_by_id(cls, librarian_id):
    return next((librarian for librarian in cls.librarian_db if librarian.librarian_id == librarian_id), None)

@classmethod
def list_librarians(cls):
    return cls.librarian_db

def assign_task(self, task):
    self.tasks.append({'task': task, 'is_completed': False})
    Librarian.task_db.append({'librarian_id': self.librarian_id, 'task': task, 'is_completed': False})

def list_tasks(self):
    return self.tasks

def get_librarian_details(self):
    return {
        "librarian_id": self.librarian_id,
        "name": self.name,
        "tasks": self.tasks,
        "is_active": self.is_active,
        "is_blocked": self.is_blocked
    }

@classmethod
def all_tasks(cls):
    return cls.task_db

@classmethod
def total_librarians(cls):
    return len(cls.librarian_db)

def list_pending_tasks(self):
    return [task for task in self.tasks if not task['is_completed']]

def list_completed_tasks(self):
    return [task for task in self.tasks if task['is_completed']]

def task_status(self, task):
    task_entry = next((t for t in self.tasks if t['task'] == task), None)
    return 'Completed' if task_entry and task_entry['is_completed'] else 'Pending'

@classmethod
def active_librarians(cls):
    return [librarian for librarian in cls.librarian_db if librarian.is_active]

@classmethod
def inactive_librarians(cls):
    return [librarian for librarian in cls.librarian_db if not librarian.is_active]

@classmethod
def blocked_librarians(cls):
    return [librarian for librarian in cls.librarian_db if librarian.is_blocked]

@classmethod
def unblocked_librarians(cls):
    return [librarian for librarian in cls.librarian_db if not librarian.is_blocked]

def check_block_status(self):
    return 'Blocked' if self.is_blocked else 'Unblocked'

def send_notification(self, message):
    # Simulate sending a notification
    print(f"Notification to {self.name}: {message}")

# Example usage
# if __name__ == "__main__":
#     librarian1 = Librarian(1, "Alice")
#     librarian2 = Librarian(2, "Bob")

#     librarian1.add_librarian()
#     librarian2.add_librarian()

#     print(Librarian.list_librarians())
#     librarian1.assign_task("Check inventory")
#     librarian1.assign_task("Order new books")
    
#     print(librarian1.list_tasks())
#     print(librarian1.get_librarian_details())
#     print(Librarian.total_librarians())

#     librarian1.tasks[0]['is_completed'] = True
#     print(librarian1.list_pending_tasks())
#     print(librarian1.list_completed_tasks())
#     print(librarian1.task_status("Check inventory"))

#     print(Librarian.active_librarians())
#     librarian1.is_active = False
#     print(Librarian.inactive_librarians())

#     librarian1.is_blocked = True
#     print(Librarian.blocked_librarians())
#     print(librarian1.check_block_status())

#     librarian1.send_notification("Your task is overdue!")