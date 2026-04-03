from flask import Blueprint, request, jsonify
from extensions import db
from models import Agency
from datetime import datetime



agency_bp = Blueprint('agency_bp', __name__)


#This route creates agency 
@agency_bp.route('/agencies', methods=['POST'])
def create_agency():
    """
    Create Agency
    ---
    tags:
      - Agency
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
              - departure_time
            properties:
              name:
                type: string
                example: Finexs Travel
              departure_time:
                type: string
                format: date-time
                example: "2026-04-05T14:30:00"
    responses:
      201:
        description: Agency created successfully
      400:
        description: Missing fields or invalid datetime format
    """

    data = request.get_json()

    name = data.get('name')
    departure_time = data.get('departure_time')

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
    """
    Get All Agencies
    ---
    tags:
      - Agency
    responses:
      200:
        description: List of agencies
    """

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
    """
    Get Agency by ID
    ---
    tags:
      - Agency
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: Agency ID
    responses:
      200:
        description: Agency found
      404:
        description: Agency not found
    """

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
    """
    Update Agency
    ---
    tags:
      - Agency
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: Agency ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                example: Updated Agency Name
              departure_time:
                type: string
                format: date-time
                example: "2026-04-06T10:00:00"
    responses:
      200:
        description: Agency updated successfully
      400:
        description: Invalid datetime format
      404:
        description: Agency not found
    """

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
    """
    Delete Agency
    ---
    tags:
      - Agency
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: Agency ID
    responses:
      200:
        description: Agency deleted successfully
      404:
        description: Agency not found
    """

    agency = db.session.get(Agency, id)

    if agency is None:
        return jsonify({"error": "Agency not found"}), 404

    db.session.delete(agency)
    db.session.commit()

    return jsonify({"message": "Agency deleted"}), 200

