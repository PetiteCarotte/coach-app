from flask import Blueprint, jsonify
from models.Program import Program

program_routes = Blueprint('program_routes', __name__)

@program_routes.route('/programs', methods=['GET'])
def get_programs():
    programs = Program.query.all()
    return jsonify([{
        'id': program.id,
        'name': program.name,
        'description': program.description,
        'duration_minutes': program.duration_minutes
    } for program in programs]), 200
