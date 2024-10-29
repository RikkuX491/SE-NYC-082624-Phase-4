from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
# class Example(db.Model):
#     __tablename__ = 'examples'

#     id = db.Column(db.Integer, primary_key=True)
#     columnname = db.Column(db.String)

# Deliverable # 1 solution code
class Hotel(db.Model, SerializerMixin):

    # Deliverable # 2 solution code
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

# Extra model for another example - Customer model
class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)