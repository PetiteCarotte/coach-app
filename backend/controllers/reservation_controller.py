""" Contrôleur pour gérer les opérations liées aux réservations."""

# pylint: disable=broad-exception-caught

from flask import jsonify, request
from services.reservation_service import (
    get_available_slots_service,
    create_reservation_service,
    cancel_reservation_service
)
def handle_get_available_slots(coach_id, date_str):
    """Gérer la récupération des créneaux disponibles."""
    try:
        available_slots = get_available_slots_service(coach_id, date_str)
        return jsonify(available_slots), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_create_reservation(data):
    """Créer une réservation."""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        result = create_reservation_service(data, token)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def handle_cancel_reservation(reservation_id):
    """Gérer l'annulation d'une réservation."""
    try:
        result = cancel_reservation_service(reservation_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
