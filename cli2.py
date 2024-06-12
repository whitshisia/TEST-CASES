from models.books import Book
from models.students import Student
from models.librarians import Librarian
from models.borrowed_records import BorrowRecord
from datetime import date


logged_in_librarian = None

def main():
    global logged_in_librarian
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            book_menu()
        elif choice == "2":
            if not logged_in_librarian:
                print("Access denied. Please log in as a librarian.")
            else:
                student_menu()
        elif choice == "3":
            if not logged_in_librarian:
                print("Access denied. Please log in as a librarian.")
            else:
                librarian_menu()
        elif choice == "4":
            borrow_record_menu()
        elif choice == "5":
            logged_in_librarian = librarian_login()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("\n===== Library Management System =====")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Book Management")
    print("2. Student Management (Librarian only)")
    print("3. Librarian Management (Librarian only)")
    print("4. Borrow Record Management")
    print("5. Librarian Login")
    print("====================================\n")

def librarian_login():
    name = input("Enter librarian name: ")
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian and librarian.name == name:
        print(f"Librarian '{name}' logged in successfully.\n")
        return librarian
    else:
        print("Invalid credentials. Please try again.\n")
        return None

# Book Management
def book_menu():
    while True:
        print("\n===== Book Management =====")
        print("1. List all books")
        print("2. Find book by title")
        print("3. Find book by author")
        print("4. Create book")
        print("5. Update book")
        print("6. Delete book")
        print("7. List available books")
        print("8. List borrowed books")
        print("9. Reserve book")
        print("10. Cancel reservation")
        print("0. Back to main menu")
        print("===========================\n")
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_title()
        elif choice == "3":
            find_book_by_author()
        elif choice == "4":
            create_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            list_available_books()
        elif choice == "8":
            list_borrowed_books()
        elif choice == "9":
            reserve_book()
        elif choice == "10":
            cancel_reservation()
        else:
            print("Invalid choice. Please try again.")

def list_books():
    print("\nListing all books:")
    books = Book.get_all()
    for book in books:
        print(book)
    print("End of list.\n")

def find_book_by_title():
    title = input("Enter book title: ")
    books = Book.find_by_title(title)
    if books:
        print(f"\nBooks with title '{title}':")
        for book in books:
            print(book)
        print("End of list.\n")
    else:
        print(f"No books found with title '{title}'.\n")

def find_book_by_author():
    author = input("Enter book author: ")
    books = Book.find_by_author(author)
    if books:
        print(f"\nBooks by author '{author}':")
        for book in books:
            print(book)
        print("End of list.\n")
    else:
        print(f"No books found by author '{author}'.\n")

def create_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    year = int(input("Enter book publication year: "))
    Book.create(title, author, genre, year)
    print(f"Book '{title}' by {author} created successfully.\n")

def update_book():
    book_id = int(input("Enter book id: "))
    book = Book.find_by_id(book_id)
    if book:
        title = input(f"Enter new title (current: {book.title}): ")
        author = input(f"Enter new author (current: {book.author}): ")
        genre = input(f"Enter new genre (current: {book.genre}): ")
        year = int(input(f"Enter new year (current: {book.year}): "))
        book.update(title, author, genre, year)
        print(f"Book ID {book_id} updated successfully.\n")
    else:
        print(f"Book with ID {book_id} not found.\n")

def delete_book():
    book_id = int(input("Enter book id: "))
    book = Book.find_by_id(book_id)
    if book:
        book.delete()
        print(f"Book with ID {book_id} deleted successfully.\n")
    else:
        print(f"Book with ID {book_id} not found.\n")

def list_available_books():
    print("\nListing all available books:")
    books = Book.list_available_books()
    for book in books:
        print(book)
    print("End of list.\n")

def list_borrowed_books():
    print("\nListing all borrowed books:")
    books = Book.list_borrowed_books()
    for book in books:
        print(book)
    print("End of list.\n")

def reserve_book():
    book_id = int(input("Enter book id: "))
    book = Book.find_by_id(book_id)
    if book and not book.is_borrowed and not book.is_reserved:
        book.reserve_book()
        print(f"Book ID {book_id} reserved successfully.\n")
    else:
        print(f"Book with ID {book_id} is either borrowed or already reserved.\n")

def cancel_reservation():
    book_id = int(input("Enter book id: "))
    book = Book.find_by_id(book_id)
    if book and book.is_reserved:
        book.cancel_reservation()
        print(f"Reservation for book ID {book_id} cancelled successfully.\n")
    else:
        print(f"Book with ID {book_id} is not reserved.\n")

# Student Management
def student_menu():
    while True:
        print("\n===== Student Management =====")
        print("1. List all students")
        print("2. Find student by name")
        print("3. Find student by id")
        print("4. Create student")
        print("5. Update student")
        print("6. Delete student")
        print("7. List borrowed books by student")
        print("8. List reserved books by student")
        print("9. Check overdue books")
        print("10. Block student")
        print("11. Unblock student")
        print("0. Back to main menu")
        print("==============================\n")
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            find_student_by_id()    
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            list_borrowed_books_by_student()
        elif choice == "8":
            list_reserved_books_by_student()
        elif choice == "9":
            check_overdue_books()
        elif choice == "10":
            block_student()
        elif choice == "11":
            unblock_student()
        else:
            print("Invalid choice. Please try again.")

def list_students():
    print("\nListing all students:")
    students = Student.get_all()
    for student in students:
        print(student)
    print("End of list.\n")

def find_student_by_name():
    name = input("Enter student name: ")
    student = Student.find_by_name(name)
    if student:
        print(f"\nStudent found: {student}\n")
    else:
        print(f"No student found with name '{name}'.\n")

def find_student_by_id():
    student_id = int(input("Enter student id: "))
    student = Student.find_by_id(student_id)
    if student:
        print(f"\nStudent found: {student}\n")
    else:
        print(f"No student found with ID {student_id}.\n")

def create_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    Student.create(name, grade)
    print(f"Student '{name}' created successfully.\n")

def update_student():
    id_ = int(input("Enter student id: "))
    if student := Student.find_by_id(id_):
        try:
            name = input(f"Enter new name (current: {student.name}): ")
            student.name = name
            grade = input(f"Enter new grade (current: {student.grade}): ")
            student.grade = grade
            student.update()
            print(f"Student ID {id_} updated successfully.\n")
        except Exception as exc:
            print("Error updating student: ",exc )
        
    else:
        print(f"Student with ID {id_} not found.\n")

def delete_student():
    student_id = int(input("Enter student id: "))
    student = Student.find_by_id(student_id)
    if student:
        student.delete()
        print(f"Student with ID {student_id} deleted successfully.\n")
    else:
        print(f"Student with ID {student_id} not found.\n")

def list_borrowed_books_by_student():
    student_id = int(input("Enter student id: "))
    books = Student.list_borrowed_books(student_id)
    if books:
        print("\nBorrowed books by student ID {}:".format(student_id))
        for book in books:
            print(book)
        print("End of list.")
    else:
        print("No borrowed books found for student ID {}.\n".format(student_id))

def list_reserved_books_by_student():
    student_id = int(input("Enter student id: "))
    books = Student.list_reserved_books(student_id)
    if books:
        print(f"\nReserved books by student ID {student_id}:")
        for book in books:
            print(book)
        print("End of list.\n")
    else:
        print(f"No reserved books found for student ID {student_id}.\n")

def check_overdue_books():
    student_id = int(input("Enter student id: "))
    books = Student.check_overdue_books_by_id(student_id)
    if books:
        print(f"\nOverdue books for student ID {student_id}:")
        for book in books:
            print(book)
        print("End of list.\n")
    else:
        print(f"No overdue books found for student ID {student_id}.\n")

def block_student():
    student_id = int(input("Enter student id: "))
    student = Student.find_by_id(student_id)
    if student:
        student.block_student()
        print(f"Student ID {student_id} blocked successfully.\n")
    else:
        print(f"Student with ID {student_id} not found.\n")

def unblock_student():
    student_id = int(input("Enter student id: "))
    student = Student.find_by_id(student_id)
    if student:
        student.unblock_student()
        print(f"Student ID {student_id} unblocked successfully.\n")
    else:
        print(f"Student with ID {student_id} not found.\n")

# Librarian Management
def librarian_menu():
    while True:
        print("\n===== Librarian Management =====")
        print("1. List all librarians")
        print("2. Find librarian by name")
        print("3. Find librarian by id")
        print("4. Create librarian")
        print("5. Update librarian")
        print("6. Delete librarian")
        print("7. Assign task")
        print("8. List tasks")
        print("9. List pending tasks")
        print("10. List completed tasks")
        print("11. Block librarian")
        print("12. Unblock librarian")
        print("0. Back to main menu")
        print("===============================\n")
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_librarians()
        elif choice == "2":
            find_librarian_by_name()
        elif choice == "3":
            find_librarian_by_id()
        elif choice == "4":
            create_librarian()
        elif choice == "5":
            update_librarian()
        elif choice == "6":
            delete_librarian()
        elif choice == "7":
            assign_task()
        elif choice == "8":
            list_tasks()
        elif choice == "9":
            list_pending_tasks()
        elif choice == "10":
            list_completed_tasks()
        elif choice == "11":
            block_librarian()
        elif choice == "12":
            unblock_librarian()
        else:
            print("Invalid choice. Please try again.")

def list_librarians():
    print("\nListing all librarians:")
    librarians = Librarian.get_all()
    for librarian in librarians:
        print(librarian)
    print("End of list.\n")

def find_librarian_by_name():
    name = input("Enter librarian name: ")
    librarian = Librarian.find_by_name(name)
    if librarian:
        print(f"\nLibrarian found: {librarian}\n")
    else:
        print(f"No librarian found with name '{name}'.\n")

def find_librarian_by_id():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        print(f"\nLibrarian found: {librarian}\n")
    else:
        print(f"No librarian found with ID {librarian_id}.\n")

def create_librarian():
    name = input("Enter librarian name: ")
    Librarian.create(name)
    print(f"Librarian '{name}' created successfully.\n")

def update_librarian():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        name = input(f"Enter new name (current: {librarian.name}): ")
        librarian.update()
        print(f"Librarian ID {librarian_id} updated successfully.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def delete_librarian():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        librarian.delete()
        print(f"Librarian with ID {librarian_id} deleted successfully.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def assign_task():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        task = input("Enter task: ")
        librarian.assign_task(task)
        print(f"Task assigned to librarian ID {librarian_id}.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def list_tasks():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        tasks = librarian.list_tasks()
        if tasks:
            print(f"\nTasks for librarian ID {librarian_id}:")
            for task in tasks:
                print(task)
            print("End of list.\n")
        else:
            print(f"No tasks found for librarian ID {librarian_id}.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def list_pending_tasks():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        tasks = librarian.list_pending_tasks()
        if tasks:
            print(f"\nPending tasks for librarian ID {librarian_id}:")
            for task in tasks:
                print(task)
            print("End of list.\n")
        else:
            print(f"No pending tasks found for librarian ID {librarian_id}.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def list_completed_tasks():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        tasks = librarian.list_completed_tasks()
        if tasks:
            print(f"\nCompleted tasks for librarian ID {librarian_id}:")
            for task in tasks:
                print(task)
            print("End of list.\n")
        else:
            print(f"No completed tasks found for librarian ID {librarian_id}.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def block_librarian():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        librarian.blocked_librarians()
        print(f"Librarian ID {librarian_id} blocked successfully.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

def unblock_librarian():
    librarian_id = int(input("Enter librarian id: "))
    librarian = Librarian.find_by_id(librarian_id)
    if librarian:
        librarian.unblocked_librarians()
        print(f"Librarian ID {librarian_id} unblocked successfully.\n")
    else:
        print(f"Librarian with ID {librarian_id} not found.\n")

# Borrow Record Management
def borrow_record_menu():
    while True:
        print("\n===== Borrow Record Management =====")
        print("1. List all borrow records")
        print("2. Find borrow record by book id")
        print("3. Find borrow record by student id")
        print("4. Create borrow record")
        print("5. Update borrow record")
        print("6. Delete borrow record")
        print("7. Check borrow status")
        print("0. Back to main menu")
        print("===================================\n")
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_borrow_records()
        elif choice == "2":
            find_borrow_record_by_book_id()
        elif choice == "3":
            find_borrow_record_by_student_id()
        elif choice == "4":
            create_borrow_record()
        elif choice == "5":
            update_borrow_record()
        elif choice == "6":
            delete_borrow_record()
        elif choice == "7":
            check_borrow_status()
        else:
            print("Invalid choice. Please try again.")

def list_borrow_records():
    print("\nListing all borrow records:")
    borrow_records = BorrowRecord.get_all()
    for record in borrow_records:
        print(record)
    print("End of list.\n")

def find_borrow_record_by_book_id():
    book_id = int(input("Enter book id: "))
    records = BorrowRecord.find_by_book_id(book_id)
    if records:
        print(f"\nBorrow records for book ID {book_id}:")
        for record in records:
            print(record)
        print("End of list.\n")
    else:
        print(f"No borrow records found for book ID {book_id}.\n")

def find_borrow_record_by_student_id():
    student_id = int(input("Enter student id: "))
    records = BorrowRecord.find_by_student_id(student_id)
    if records:
        print(f"\nBorrow records for student ID {student_id}:")
        for record in records:
            print(record)
        print("End of list.\n")
    else:
        print(f"No borrow records found for student ID {student_id}.\n")

def create_borrow_record():
    book_id = int(input("Enter book id: "))
    student_id = int(input("Enter student id: "))
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    BorrowRecord.create(book_id, student_id, borrow_date, due_date)
    print("Borrow record created successfully.\n")

def update_borrow_record():
    record_id = int(input("Enter borrow record id: "))
    record = BorrowRecord.find_by_id(record_id)
    if record:
        return_date = input(f"Enter return date (current: {record.return_date}): ")
        is_returned = input(f"Is returned? (current: {record.is_returned}): ").lower() in ['true', '1', 'yes']
        record.update(return_date, is_returned)
        print(f"Borrow record ID {record_id} updated successfully.\n")
    else:
        print(f"Borrow record with ID {record_id} not found.\n")

def delete_borrow_record():
    record_id = int(input("Enter borrow record id: "))
    record = BorrowRecord.find_by_id(record_id)
    if record:
        record.delete()
        print(f"Borrow record with ID {record_id} deleted successfully.\n")
    else:
        print(f"Borrow record with ID {record_id} not found.\n")

def check_borrow_status():
    record_id = int(input("Enter borrow record id: "))
    record = BorrowRecord.find_by_id(record_id)
    if record:
        status = record.borrow_status()
        print(f"Borrow status for record ID {record_id}: {status}\n")
    else:
        print(f"Borrow record with ID {record_id} not found.\n")

# Exit the program
def exit_program():
    print("Exiting the program ...")
    exit(0)

if __name__ == "__main__":
    main()
