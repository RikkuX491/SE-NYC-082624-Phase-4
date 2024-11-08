#!/usr/bin/env python3

from app import app, bcrypt
from models import db, Hotel, User, Review

with app.app_context():
    Hotel.query.delete()
    User.query.delete()
    Review.query.delete()

    hotel1 = Hotel(name="Marriott", image="/images/marriott.png")
    hotel2 = Hotel(name="Waikiki Resort", image="/images/waikiki-resort.png")
    hotel3 = Hotel(name="Bahamas Resort", image="/images/bahamas-resort.png")

    password_1 = "ab123"
    encrypted_password_1 = bcrypt.generate_password_hash(password_1).decode('utf-8')
    user1 = User(first_name="Alice", last_name="Baker", username="alicebaker123", password_hash=encrypted_password_1, type="customer")

    password_2 = "flatironschool"
    encrypted_password_2 = bcrypt.generate_password_hash(password_2).decode('utf-8')
    user2 = User(first_name="Bob", last_name="Carris", username="bobcarris456", password_hash=encrypted_password_2, type="customer")
    
    password_3 = "python"
    encrypted_password_3 = bcrypt.generate_password_hash(password_3).decode('utf-8')
    user3 = User(first_name="Cynthia", last_name="Dawson", username="cynthiadawson789", password_hash=encrypted_password_3, type="customer")
    
    password_4 = "bahamas"
    encrypted_password_4 = bcrypt.generate_password_hash(password_4).decode('utf-8')
    user4 = User(first_name="Daniel", last_name="Evans", username="danielevans101", password_hash=encrypted_password_4, type="admin")

    review1 = Review(rating=5, text="Best hotel ever!", hotel_id=1, user_id=1)
    review2 = Review(rating=4, text="Amazing!", hotel_id=1, user_id=2)
    review3 = Review(rating=4, text="Great!", hotel_id=2, user_id=1)
    review4 = Review(rating=3, text="Not as good as the first time I was there.", hotel_id=1, user_id=1)
    
    db.session.add_all([hotel1, hotel2, hotel3])
    db.session.add_all([user1, user2, user3, user4])
    db.session.add_all([review1, review2, review3, review4])

    db.session.commit()
    print("🌱 Hotels, Users, and Reviews successfully seeded! 🌱")