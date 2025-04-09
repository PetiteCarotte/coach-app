from flask import Blueprint, request, jsonify, session
from flask_cors import CORS
from utils.db import app, db
from controllers.user_controller import register_user
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
    return register_user(data)

# Route de connexion
@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        #afficher l'utilisateur connecté
        print(f"Utilisateur connecté: {user.first_name} {user.last_name}")
        #afficher l'ID de l'utilisateur connecté
        print(f"ID de l'utilisateur connecté: {user.id}")
        session['user_id'] = user.id  # Stocker l'ID de l'utilisateur dans la session
        # afficher l'ID de la session
        print(f"ID de la session: {session['user_id']}")
        print(session)
        token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, SECRET_KEY, algorithm="HS256")
        print(f"Token JWT: {token}")
        return jsonify({'message': 'Connexion réussie !TOKE', 'token': token}), 200
    else:
        return jsonify({'error': 'Email ou mot de passe incorrect.'}), 401

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