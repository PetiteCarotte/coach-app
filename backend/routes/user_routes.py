from flask import Blueprint, request, jsonify, session
from flask_cors import CORS
from utils.db import app, db
from controllers.user_controller import handle_register_user, handle_login_user
from models.User import User, Client, Coach
import jwt
import datetime

SECRET_KEY = 'supersecretkey' 

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def hello():
    return "Hello World!"

# Création du Blueprint pour les utilisateurs
user_routes = Blueprint('user_routes', __name__)

# Route d'inscription
@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return handle_register_user(data)

# Route de connexion
@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return handle_login_user(data)

# Route de déconnexion
@user_routes.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Supprimer l'ID de l'utilisateur de la session
    return jsonify({'message': 'Déconnexion réussie !'}), 200

# Route protégée
@user_routes.route('/dashboard', methods=['GET'])
def dashboard(user_id):
    # Vérifier si l'utilisateur est connecté
    if 'user_id' not in session:
        return jsonify({'error': 'Utilisateur non connecté.'}), 401

    user = User.query.get(session['user_id'])
    if user:
        return jsonify({'message': f'Bienvenue {user.first_name} !', 'role': user.role}), 200
    else:
        return jsonify({'error': 'Utilisateur non trouvé.'}), 404