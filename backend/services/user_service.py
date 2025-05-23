""" Service pour la gestion des utilisateurs et de l'authentification."""

# pylint: disable=too-many-arguments, too-many-positional-arguments, too-many-boolean-expressions, too-many-return-statements, broad-exception-caught, raise-missing-from

import datetime
import jwt
from sqlalchemy.exc import IntegrityError
from models.user import User
from models.slot import Slot
from models.coach_available_slot import CoachAvailableSlot
from utils.db import db
from factories.user_factory import UserFactory
from strategies.user_strategies import ClientStrategy

SECRET_KEY = 'supersecretkey'

def register_new_user(first_name, last_name, email, password, confirm_password, role):
    """ Inscription d'un nouvel utilisateur """

    if not all([first_name, last_name, email, password, confirm_password, role]):
        return {'error': 'Tous les champs sont requis.'}, 400

    if password != confirm_password:
        return {'error': 'Les mots de passe ne correspondent pas.'}, 400

    if len(password) < 6:
        return {'error': 'Le mot de passe doit comporter au moins 6 caractères.'}, 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {'error': 'Cet email est déjà utilisé.'}, 400

    try:
        new_user = UserFactory.create_user(role, first_name, last_name, email, password)

        role_action = new_user.strategy.perform_action() # Utilisation de la stratégie
        print(f"Action spécifique pour le rôle {role}: {role_action}")
        if role == "Coach":

            db.session.add(new_user)
            db.session.flush()

            default_slot_ids = [1, 2, 3, 4, 7, 8, 9, 10]
            for slot_id in default_slot_ids:
                slot = Slot.query.get(slot_id)
                if slot:
                    availability = CoachAvailableSlot(coach_id=new_user.id, slot_id=slot.id)
                    db.session.add(availability)

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'Inscription réussie !', 'role_action': role_action}, 201

    except IntegrityError:
        db.session.rollback()
        return {'error': 'Erreur d\'intégrité de la base de données.'}, 500
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500

def authenticate_user(email, password):
    """ Authentifier l'utilisateur et retourner l'objet utilisateur ainsi que le jeton JWT """

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm="HS256")
        return user, token
    return None, None

def get_reservations_for_client(client_id):
    """Récupérer les réservations pour un client donné."""

    return ClientStrategy.view_reservations(client_id)
