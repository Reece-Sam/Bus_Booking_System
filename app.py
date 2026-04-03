from flask import Flask
from flasgger import Swagger
from extensions import db
from models import User, Agency, Booking
from routes.user import user_bp   
from routes.booking import booking_bp
from routes.agency import agency_bp
from dotenv import load_dotenv

import os

load_dotenv()
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kange24@localhost/bus_booking'
app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Swagger(app)

# register routes
app.register_blueprint(user_bp)

app.register_blueprint(booking_bp)

app.register_blueprint(agency_bp)


# Create tables
with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route('/')
def home():
    return "Bus Booking System Running"

if __name__ == "__main__":
    app.run(debug=True)