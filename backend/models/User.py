"""Définit les modèles User, Client et Coach."""

# pylint: disable=too-many-positional-arguments, disable=too-many-arguments, missing-function-docstring, too-many-function-args

from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db

class User(db.Model):
    """Modèle pour les utilisateurs."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'Client' or 'Coach'
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, first_name, last_name, email, password, role=None):
        """Initialise un nouvel utilisateur avec mot de passe hashé."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        """Vérifie si le mot de passe correspond au hash."""

        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Retourne une représentation dictionnaire de l'utilisateur."""

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role": self.role
        }

class Client(User):
    """Modèle pour les clients."""

    __mapper_args__ = {
        'polymorphic_identity': 'Client',
    }

class Coach(User):
    """Modèle pour les coachs."""

    __mapper_args__ = {
        'polymorphic_identity': 'Coach',
    }
