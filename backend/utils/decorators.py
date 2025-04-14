""" Module de décorateurs pour la gestion des erreurs et de l'authentification. """

from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = 'supersecretkey'

def requires_auth(f):
    """Décorateur pour vérifier l'authentification via JWT."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            return jsonify({'error': 'Token manquant'}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expiré'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token invalide'}), 401
        return f(*args, **kwargs)
    return decorated
