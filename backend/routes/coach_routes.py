from flask import Blueprint, jsonify
from controllers.coach_controller import handle_get_coaches

coach_routes = Blueprint('coach_routes', __name__)

@coach_routes.route('/coaches', methods=['GET'])
def get_coaches():
    """Récupérer la liste des coachs."""
    
    return handle_get_coaches()
