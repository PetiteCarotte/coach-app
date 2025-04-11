# controllers/user_controller.py
from flask import jsonify, session
from services.user_service import authenticate_user, register_new_user

def handle_register_user(data):
    """ Inscription d'un nouvel utilisateur """

    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    role = data.get('role')

    result, status = register_new_user(first_name, last_name, email, password, confirm_password, role)
    return jsonify(result), status

def handle_login_user(data):
    """ Connexion d'un utilisateur """

    email = data.get('email')
    password = data.get('password')

    user, token = authenticate_user(email, password)
    if user:
        session['user_id'] = user.id
        return jsonify({'message': 'Connexion réussie !', 'token': token}), 200
    else:
        return jsonify({'error': 'Email ou mot de passe incorrect.'}), 401
