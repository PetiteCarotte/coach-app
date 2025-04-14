""" Contrôleur pour gérer les programmes d'entraînement."""

from services.program_service import get_programs_service
from flask import jsonify

def handle_get_programs():
    """Gérer la récupération des programmes."""
    try:
        programs = get_programs_service()
        return jsonify([{
            'id': program.id,
            'name': program.name,
            'description': program.description,
            'duration_minutes': program.duration_minutes
        } for program in programs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
