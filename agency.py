from flask import Blueprint, request, jsonify
from extensions import db
from models import Agency
from datetime import datetime



agency_bp = Blueprint('agency_bp', __name__)


#This route creates agency 
@agency_bp.route('/agencies', methods=['POST'])
def create_agency():
    data = request.get_json()

    name = data.get('name')
    departure_time = data.get('departure_time')  # expect ISO format string

    if not name or not departure_time:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        departure_time = datetime.fromisoformat(departure_time)
    except ValueError:
        return jsonify({"error": "Invalid datetime format"}), 400

    agency = Agency(
        name=name,
        departure_time=departure_time
    )

    db.session.add(agency)
    db.session.commit()

    return jsonify({
        "message": "Agency created",
        "agency": {
            "id": agency.id,
            "name": agency.name,
            "departure_time": agency.departure_time
        }
    }), 201


#This route gets all agency
@agency_bp.route('/agencies', methods=['GET'])
def get_agencies():
    agencies = Agency.query.all()

    result = []
    for agency in agencies:
        result.append({
            "id": agency.id,
            "name": agency.name,
            "departure_time": agency.departure_time
        })

    return jsonify(result), 200


#This routes gets agency by Id
@agency_bp.route('/agencies/<int:id>', methods=['GET'])
def get_agency(id):
    agency = db.session.get(Agency, id)

    if agency is None:
        return jsonify({"error": "Agency not found"}), 404

    return jsonify({
        "id": agency.id,
        "name": agency.name,
        "departure_time": agency.departure_time
    }), 200


#This route updates agency by Id
@agency_bp.route('/agencies/<int:id>', methods=['PATCH'])
def update_agency(id):
    agency = db.session.get(Agency, id)

    if agency is None:
        return jsonify({"error": "Agency not found"}), 404

    data = request.get_json()

    if 'name' in data:
        agency.name = data['name']

    if 'departure_time' in data:
        try:
            agency.departure_time = datetime.fromisoformat(data['departure_time'])
        except ValueError:
            return jsonify({"error": "Invalid datetime format"}), 400

    db.session.commit()

    return jsonify({
        "message": "Agency updated",
        "agency": {
            "id": agency.id,
            "name": agency.name,
            "departure_time": agency.departure_time
        }
    }), 200


#This route deletes agency by id 
@agency_bp.route('/agencies/<int:id>', methods=['DELETE'])
def delete_agency(id):
    agency = db.session.get(Agency, id)

    if agency is None:
        return jsonify({"error": "Agency not found"}), 404

    db.session.delete(agency)
    db.session.commit()

    return jsonify({"message": "Agency deleted"}), 200


