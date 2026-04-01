from flask import Blueprint, request , jsonify 
from extensions import db
from models import Booking

booking_bp = Blueprint('booking_bp', __name__)

#This route creates a booking
@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()