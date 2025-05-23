""" Routes pour la gestion des réservations. """

from flask import Blueprint, request, jsonify
from controllers.reservation_controller import (
    handle_get_available_slots,
    handle_create_reservation,
    handle_cancel_reservation
)
from utils.decorators import requires_auth

reservation_routes = Blueprint('reservation_routes', __name__)

@reservation_routes.route('/available_slots', methods=['GET'])
def get_available_slots():
    """Récupérer les créneaux disponibles pour un coach à une date donnée."""
    coach_id = request.args.get('coach_id', type=int)
    date_str = request.args.get('date', type=str)

    if not coach_id or not date_str:
        return jsonify({"error": "Missing coach_id or date parameter"}), 400

    return handle_get_available_slots(coach_id, date_str)

@reservation_routes.route('/reservations', methods=['POST'])
@requires_auth
def create_reservation():
    """Créer une réservation."""
    data = request.get_json()
    required_fields = ['coach_id', 'program_id', 'slot_id', 'date']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Champs manquants'}), 400

    return handle_create_reservation(data)

@reservation_routes.route('/reservations/<int:reservation_id>', methods=['DELETE'])
@requires_auth
def cancel_reservation(reservation_id):
    """Annuler une réservation."""
    return handle_cancel_reservation(reservation_id)
