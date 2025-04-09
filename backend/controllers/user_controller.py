
from flask import jsonify
from models.User import User, Client, Coach
from models.Slot import Slot
from models.CoachAvailableSlot import CoachAvailableSlot
from models.Program import Program
from utils.db import db
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

"""
    user_controller.py
    Fichier contenant les contrôleurs pour gérer les utilisateurs.
    Ce fichier contient la logique pour l'inscription des utilisateurs, y compris la validation des données et la gestion des erreurs.
"""
# USER CONTROLLER -> Inscription d'un utilisateur
# POST /api/register
def register_user(data):
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    role = data.get('role')

    # Log des valeurs extraites
    print(f"Extracted data: firstName={first_name}, lastName={last_name}, email={email}, role={role}")

    # Validation des champs
    if not first_name or not last_name or not email or not password or not confirm_password or not role:
        return jsonify({'error': 'Tous les champs sont requis.'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Les mots de passe ne correspondent pas.'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Le mot de passe doit comporter au moins 6 caractères.'}), 400

    # Vérifier si l'email est déjà pris
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Cet email est déjà utilisé.'}), 400

    try:
        # Créer l'utilisateur en fonction de son rôle
        if role == "Client":
            new_user = Client(first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_user)

        elif role == "Coach":
            new_user = Coach(first_name=first_name, last_name=last_name, email=email, password=password)
        
            db.session.add(new_user)
            db.session.flush()  # Pour avoir l'ID du coach généré

            # Slots par défaut (1, 2, 3, 4, 7, 8, 9, 10)
            default_slot_ids = [1, 2, 3, 4, 7, 8, 9, 10]
            for slot_id in default_slot_ids:
                slot = Slot.query.get(slot_id)
                if slot:
                    availability = CoachAvailableSlot(coach_id=new_user.id, slot_id=slot.id)
                    db.session.add(availability)


        else:
            return jsonify({'error': 'Rôle invalide.'}), 400

        db.session.commit()

        return jsonify({'message': 'Inscription réussie !'}), 201
    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {str(e)}")
        return jsonify({'error': 'Erreur d\'intégrité de la base de données.'}), 500
    except Exception as e:
        db.session.rollback()
        print(f"Exception: {str(e)}")
        return jsonify({'error': str(e)}), 500





