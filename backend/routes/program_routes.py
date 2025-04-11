from flask import Blueprint, jsonify
from controllers.program_controller import handle_get_programs

program_routes = Blueprint('program_routes', __name__)

@program_routes.route('/programs', methods=['GET'])
def get_programs():
    return handle_get_programs()
