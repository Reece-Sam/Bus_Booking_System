from flask import Blueprint, request , jsonify 
from extensions import db
from models import Booking, Agency, User
from datetime import datetime, timedelta



booking_bp = Blueprint('booking_bp', __name__)


#This route creates a booking
@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()

    user_id = data.get('user_id')
    agency_id = data.get('agency_id')
    price = data.get('price')

    if not user_id or not agency_id or not price:
        return jsonify({"error": "Missing required fields"}), 400

    booking = Booking(
        user_id=user_id,
        agency_id=agency_id,
        price=price
    )

    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "message": "Booking created",
        "booking": {
            "id": booking.id,
            "user_id": booking.user_id,
            "agency_id": booking.agency_id,
            "price": str(booking.price),
            "is_cancelled": booking.is_cancelled,
            "created_at": booking.created_at,
            "updated_at": booking.updated_at
        }
    }), 201



#This route gets all booking 
@booking_bp.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()

    result = []
    for booking in bookings:
        result.append({
            "id": booking.id,
            "user_id": booking.user_id,
            "agency_id": booking.agency_id,
            "price": str(booking.price),
            "is_cancelled": booking.is_cancelled,
            "created_at": booking.created_at,
            "updated_at": booking.updated_at
        })

    return jsonify(result), 200


#This routes gets booking by on Id 
@booking_bp.route('/bookings/<int:id>', methods=['GET'])
def get_booking(id):
    booking = db.session.get(Booking, id)

    if booking is None:
        return jsonify({"error": "Booking not found"}), 404

    return jsonify({
        "id": booking.id,
        "user_id": booking.user_id,
        "agency_id": booking.agency_id,
        "price": str(booking.price),
        "is_cancelled": booking.is_cancelled,
        "created_at": booking.created_at,
        "updated_at": booking.updated_at
    }), 200


#This route updates or cancels booking by Id 
@booking_bp.route('/bookings/<int:id>/cancel', methods=['PATCH'])
def cancel_booking(id):
    booking = db.session.get(Booking, id)

    if booking is None:
        return jsonify({"error": "Booking not found"}), 404

    if booking.is_cancelled:
        return jsonify({"message": "Booking already cancelled"}), 400

    agency = db.session.get(Agency, booking.agency_id)
    if not agency:
        return jsonify({"error": "Agency not found"}), 404

    departure_time = booking.agency.departure_time
    now = datetime.now()

     #The 3hrs cancelation policy
    if departure_time - now < timedelta(hours=3):
        return jsonify({
            "error": "Cannot cancel less than 3 hours before departure"
        }), 400

    booking.is_cancelled = True
    db.session.commit()

    return jsonify({
        "message": "Booking cancelled successfully",
        "booking_id": booking.id
    }), 200




#This routes updates booking by Id
@booking_bp.route('/bookings/<int:id>', methods=['PATCH'])
def update_booking(id):
    data = request.get_json()

    booking = db.session.get(Booking, id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    if 'price' in data:
        booking.price = data['price']

    if 'user_id' in data:
        user = db.session.get(User, data['user_id'])
        if not user:
            return jsonify({"error": "User not found"}), 404
        booking.user_id = data['user_id']

    if 'agency_id' in data:
        agency = db.session.get(Agency, data['agency_id'])
        if not agency:
            return jsonify({"error": "Agency not found"}), 404
        booking.agency_id = data['agency_id']

    db.session.commit()

    return jsonify({
        "message": "Booking updated successfully",
        "booking": {
            "id": booking.id,
            "price": booking.price,
            "user": booking.user.name,
            "agency": booking.agency.name,
            "departure_time": booking.agency.departure_time.isoformat(),
            "is_cancelled": booking.is_cancelled
        }
    }), 200



#This routes deletes booking by Id 
@booking_bp.route('/bookings/<int:id>', methods=['DELETE'])
def delete_booking(id):
    booking = db.session.get(Booking, id)

    if booking is None:
        return jsonify({"error": "Booking not found"}), 404

    db.session.delete(booking)
    db.session.commit()

    return jsonify({"message": "Booking deleted"}), 200