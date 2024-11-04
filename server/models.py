from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

# contains definitions of tables and associated schema constructs
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model. SerializerMixin allows for calling the to_dict() method on an instance which will return a dictionary with keys are value pairs for each db.Column. db.relationships are also serialized
class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    @validates('name')
    def validate_name(self, column, value):
        if type(value) == str and 5 <= len(value) <= 50:
            return value
        else:
            raise Exception(f"{column} must be a string that is between 5 and 50 characters long!")

    # 1 hotel has many reviews: 1-to-many relationship between hotels and reviews tables
    reviews = db.relationship('Review', back_populates='hotel', cascade='all')

    # hotels and customers Many-to-Many relationship: The hotel's customers
    customers = association_proxy('reviews', 'customer', creator = lambda c: Review(customer = c))

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    __table_args__ = (db.CheckConstraint('first_name != last_name'),)

    @validates('first_name', 'last_name')
    def validate_customer_columns(self, column, value):
        if type(value) == str and 3 <= len(value) <= 15:
            return value
        else:
            raise Exception(f"{column} must be a string that is between 3 and 15 characters long!")
        
    # @validates('last_name')
    # def validate_last_name(self, column, value):
    #     if type(value) == str and 3 <= len(value) <= 15:
    #         return value
    #     else:
    #         raise Exception(f"{column} must be a string that is between 3 and 15 characters long!")

    # 1 customer has many reviews: 1-to-many relationship between customers and reviews tables
    reviews = db.relationship('Review', back_populates='customer', cascade='all')

    # hotels and customers Many-to-Many relationship: The customer's hotels
    hotels = association_proxy('reviews', 'hotel', creator = lambda h: Review(hotel = h))

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String, nullable=False)

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

    # A review belongs to a hotel: 1-to-many relationship between hotels and reviews tables
    hotel = db.relationship('Hotel', back_populates='reviews')

    # A review belongs to a customer: 1-to-many relationship between customers and reviews tables
    customer = db.relationship('Customer', back_populates='reviews')

    @validates('rating')
    def validate_rating(self, column, value):
        if type(value) == int and 1 <= value <= 5:
            return value
        raise Exception(f"{column} must be an integer between 1 and 5!")
    
    @validates('text')
    def validate_text(self, column, value):
        if type(value) == str and 3 <= len(value) <= 100:
            return value
        else:
            raise Exception(f"{column} must be a string that is between 3 and 100 characters long!")
        
    @validates('hotel_id', 'customer_id')
    def validate_foreign_key_columns(self, column, value):
        if type(value) == int:
            return value
        else:
            raise TypeError(f"{column} must be an integer!")