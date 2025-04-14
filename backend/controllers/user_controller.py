""" Contrôleur pour gérer les utilisateurs et les réservations. """

from flask import jsonify, session, request
from services.user_service import authenticate_user, register_new_user, get_reservations_for_client
import jwt

SECRET_KEY = 'supersecretkey'

def handle_register_user(data):
    """Gérer l'inscription d'un nouvel utilisateur."""
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    role = data.get('role')

    result, status = register_new_user(first_name, last_name, email, password, confirm_password, role)
    return jsonify(result), status

def handle_login_user(data):
    """Gérer la connexion d'un utilisateur."""
    email = data.get('email')
    password = data.get('password')

    user, token = authenticate_user(email, password)
    if user:
        session['user_id'] = user.id
        return jsonify({'message': 'Connexion réussie !', 'token': token}), 200
    else:
        return jsonify({'error': 'Email ou mot de passe incorrect.'}), 401

def handle_get_my_reservations(request):
    """Gérer la récupération des réservations du client connecté."""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        client_id = decoded.get('user_id')

        # Appeler le service pour récupérer les réservations
        reservations = get_reservations_for_client(client_id)

        return jsonify(reservations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
