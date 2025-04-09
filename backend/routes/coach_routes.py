from flask import Blueprint, jsonify
from models.User import Coach

coach_routes = Blueprint('coach_routes', __name__)

@coach_routes.route('/coaches', methods=['GET'])
def get_coaches():
    coaches = Coach.query.all()
    return jsonify([coach.to_dict() for coach in coaches]), 200
