""" Controleur pour gérer les opérations liées aux coachs."""

# pylint: disable=broad-exception-caught

from flask import jsonify
from services.coach_service import get_coaches_service

def handle_get_coaches():
    """Gérer la récupération des coachs."""
    try:
        coaches = get_coaches_service()
        return jsonify([coach.to_dict() for coach in coaches]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
