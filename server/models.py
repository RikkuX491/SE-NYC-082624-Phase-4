from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

# contains definitions of tables and associated schema constructs
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'

    # Use serialize_only to include columns that will be serialized with the to_dict() method
    # serialize_only = ('id',)
    # serialize_only = ('id', 'name')

    # Use serialize_rules to exclude columns that will not be serialized with the to_dict() method
    # serialize_rules = ('-reviews',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='hotel', cascade='all')

    # Association Proxy (Many-to-Many relationship - This is the Hotel has many Customers part of the Many-to-Many relationship)
    customers = association_proxy('reviews', 'customer', creator=lambda c: Review(customer=c))

    # def reviews(self):
    #     return [review for review in Review.query.all() if review.hotel_id == self.id]

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='customer', cascade='all')

    # Association Proxy (Many-to-Many relationship - This is the Customer has many Hotels part of the Many-to-Many relationship)
    hotels = association_proxy('reviews', 'hotel', creator=lambda h: Review(hotel=h))

# Deliverable # 1 solution code
class Review(db.Model, SerializerMixin):

    # Deliverable # 2 solution code
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.String)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    hotel = db.relationship('Hotel', back_populates='reviews')
    customer = db.relationship('Customer', back_populates='reviews')

    # def hotel(self):
    #     hotels = [hotel for hotel in Hotel.query.all() if hotel.id == self.hotel_id]
        
    #     if len(hotels) > 0:
    #         return hotels[0]
    #     else:
    #         return None