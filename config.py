# import sqlite3
# CONN = sqlite3.connect('library.db')
# CURSOR = CONN.cursor()


# class Database:
#     def create_tables(self):
#         sql1 = """
#         CREATE TABLE IF NOT EXISTS students(
#         id INTEGER PRIMARY KEY, 
#         name varchar(40),
#         email varchar(40),
#         books_borrowed(INTEGER),
#         faculty varchar(60)),
#         """
#         CURSOR.execute(sql1)

#         sql2 = """CREATE TABLE IF NOT EXISTS librarians(
#         id INTEGER PRIMARY KEY, 
#         first_name varchar(40), 
#         last_name varchar(40), 
#         contact INTEGER,
#         username varchar(40),
#         password varchar(40))"""
#         CURSOR.execute(sql2)

#         sql3 = """CREATE TABLE IF NOT EXISTS borrowed
#         _records(
#         id INTEGER PRIMARY KEY,
#         loan_date INTEGER,
#         due_date INTEGER,
#         return_date INTEGER,
#         book_id INTEGER,
#         student_id INTEGER,

#         FOREIGN KEY(student_id) REFERENCES students(id),
#         FOREIGN KEY(book_id) REFERENCES books(id))"""
#         CURSOR.execute(sql3)

#         sql4 = """CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY,
#         year INTEGER,
#         title varchar(40),
#         author varchar(40),
#         publisher varchar(40),
#         isbn INTEGER,
#         category varchar(40),
#         available_copies INTEGER,
#         total_copies INTEGER
#         )"""
#         CURSOR.execute(sql4)

#         CONN.commit()


#     def drop_tables(self):
#         sql = """DROP TABLE IF EXISTS students"""
#         CURSOR.execute(sql)

#         sql = """DROP TABLE IF EXISTS librarians"""
#         CURSOR.execute(sql)

#         sql = """DROP TABLE IF EXISTS borrowed_records"""
#         CURSOR.execute(sql)

#         sql = """DROP TABLE IF EXISTS books"""
#         CURSOR.execute(sql)
#         CONN.commit()


# db = Database()

# # db.drop_tables()
# # print("***********Dropped Tables*****************")

# print("***********Creating Tables-------->")
# db.create_tables()
# print("***********3 Tables Created*****************")