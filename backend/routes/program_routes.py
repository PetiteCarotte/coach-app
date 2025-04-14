"""Routes pour gérer les programmes."""

from flask import Blueprint
from controllers.program_controller import handle_get_programs

program_routes = Blueprint('program_routes', __name__)

@program_routes.route('/programs', methods=['GET'])
def get_programs():
    """Récupérer la liste des programmes."""
    return handle_get_programs()
