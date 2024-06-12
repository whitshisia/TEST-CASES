# from datetime import date, timedelta

# # Add a new book
# def add_book(title, author, isbn, publisher, year, category, total_copies):
#     book = Book(title=title, author=author, isbn=isbn, publisher=publisher, year=year, category=category, available_copies=total_copies, total_copies=total_copies)
#     session.add(book)
#     session.commit()

# # Add a new student
# def add_student(first_name, last_name, student_class, contact):
#     student = Student(first_name=first_name, last_name=last_name, student_class=student_class, contact=contact)
#     session.add(student)
#     session.commit()

# # Issue a book to a student
# def issue_book(book_id, student_id):
#     book = session.query(Book).filter_by(book_id=book_id).first()
#     if book and book.available_copies > 0:
#         loan = Loan(book_id=book_id, student_id=student_id, loan_date=date.today(), due_date=date.today() + timedelta(days=14))
#         book.available_copies -= 1
#         session.add(loan)
#         session.commit()
#     else:
#         print("Book not available")

# # Return a book from a student
# def return_book(loan_id):
#     loan = session.query(Loan).filter_by(loan_id=loan_id).first()
#     if loan and not loan.return_date:
#         loan.return_date = date.today()
#         book = session.query(Book).filter_by(book_id=loan.book_id).first()
#         book.available_copies += 1
#         session.commit()
#     else:
#         print("Invalid loan ID or book already returned")

# # View all books
# def view_books():
#     books = session.query(Book).all()
#     for book in books:
#         print(book.title, book.author, book.available_copies, book.total_copies)

# # View all students
# def view_students():
#     students = session.query(Student).all()
#     for student in students:
#         print(student.first_name, student.last_name, student.student_class, student.contact)

# # View all loans
# def view_loans():
#     loans = session.query(Loan).all()
#     for loan in loans:
#         print(loan.loan_id, loan.book.title, loan.student.first_name, loan.loan_date, loan.due_date, loan.return_date)

# # Example usage
# add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Scribner", 1925, "Fiction", 5)
# add_student("John", "Doe", "10th Grade", "555-1234")
# issue_book(1, 1)
# view_books()
# view_students()
# view_loans()
