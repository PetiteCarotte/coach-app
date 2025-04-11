from flask import Blueprint, request, jsonify
from controllers.reservation_controller import handle_get_available_slots, handle_create_reservation

reservation_routes = Blueprint('reservation_routes', __name__)

# Obtenir les créneaux disponibles pour un coach à une date donnée
@reservation_routes.route('/available_slots', methods=['GET'])
def get_available_slots():
    coach_id = request.args.get('coach_id', type=int)
    date_str = request.args.get('date', type=str)

    if not coach_id or not date_str:
        return jsonify({"error": "Missing coach_id or date parameter"}), 400

    return handle_get_available_slots(coach_id, date_str)

# Créer une réservation
@reservation_routes.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    required_fields = ['coach_id', 'program_id', 'slot_id', 'date']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Champs manquants'}), 400

    return handle_create_reservation(data)
