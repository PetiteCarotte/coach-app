from flask import Blueprint, request, jsonify, session, g
from flask_cors import CORS
from utils.db import app, db
from controllers.user_controller import handle_register_user, handle_login_user, handle_get_my_reservations
from models.User import User, Client, Coach
from models.Reservation import Reservation
from models.Program import Program
from models.Slot import Slot
import jwt
import datetime
from factories.user_factory import UserFactory
from strategies.user_strategies import ClientStrategy

SECRET_KEY = 'supersecretkey' 

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Création du Blueprint pour les utilisateurs
user_routes = Blueprint('user_routes', __name__)

@app.route('/')
def hello():
    return "Hello World!"

# Route d'inscription
@user_routes.route('/register', methods=['POST'])
def register():
    """Inscription d'un nouvel utilisateur."""

    data = request.get_json()
    return handle_register_user(data)

# Route de connexion
@user_routes.route('/login', methods=['POST'])
def login():
    """Connexion d'un utilisateur."""

    data = request.get_json()
    return handle_login_user(data)

# Route de déconnexion
@user_routes.route('/logout', methods=['POST'])
def logout():
    """Déconnexion de l'utilisateur."""

    session.pop('user_id', None)  # Supprimer l'ID de l'utilisateur de la session
    return jsonify({'message': 'Déconnexion réussie !'}), 200

# Route pour récupérer les réservations de l'utilisateur connecté
@user_routes.route('/my_reservations', methods=['GET'])
def get_my_reservations():
    """Récupérer les réservations du client connecté."""

    return handle_get_my_reservations(request)