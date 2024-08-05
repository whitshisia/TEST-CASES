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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    # add relationship
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan', overlaps="pizzas")
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants', overlaps="restaurant_pizzas")

    # add serialization rules
    serialize_rules = ('-restaurant_pizzas.restaurant', '-restaurant_pizzas.pizza')

    def __repr__(self):
        return f"<Restaurant {self.name}>"


class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    # add relationship
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan', overlaps="restaurants")
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas', overlaps="restaurant_pizzas")

    # add serialization rules
    serialize_rules = ('-restaurant_pizzas.pizza', '-restaurant_pizzas.restaurant')

    def __repr__(self):
        return f"<Pizza {self.name}, {self.ingredients}>"


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # add relationships
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id", ondelete="CASCADE"))

    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas', overlaps="restaurants")
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas', overlaps="pizzas")

    # add serialization rules
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')

    # add validation
    @validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        return price

    def __repr__(self):
        return f"<RestaurantPizza ${self.price}>"
