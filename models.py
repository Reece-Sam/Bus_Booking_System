from datetime import datetime
from sqlalchemy import func 
from extensions import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime,
        server_default=func.now(), 
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=func.now(), 
        onupdate=func.now(), 
        nullable=False
    )
    name = db.Column(db.String(100))
    phone_number = db.Column(db.String(100), nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def __repr__(self):
        return f'<User: {self.name}>'


class Agency(db.Model):
    __tablename__ = "agencies"  # Explicitly naming the table
    
    id = db.Column(db.Integer, primary_key=True)
    # Using server_default ensures the database handles the timezone generation
    name = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    bookings = db.relationship('Booking', backref='agency', lazy=True)


class Booking(db.Model):
    __tablename__ = "bookings"  # Explicitly naming the table
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime,
        server_default=func.now(), 
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=func.now(), 
        onupdate=func.now(), 
        nullable=False
    )
    
    price = db.Column(db.Numeric(10, 2), nullable=False)
    is_cancelled = db.Column(db.Boolean, nullable=False, default=False)
    # name = db.Column(db.String(100), nullable=False)

    # Pointing exactly to the __tablename__ strings defined above
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'), nullable=False)

    # These use the Python Class Names to establish ORM relationships
    user = db.relationship('User', backref='bookings')
    agency = db.relationship('Agency', backref='bookings')
