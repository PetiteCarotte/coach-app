from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

# Base User Model
class User(db.Model):
    """ Modèle pour les utilisateurs. """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'Client' or 'Coach'
    __mapper_args__ = {
        'polymorphic_identity': 'user',  # Base class identity
        'polymorphic_on': role           # Column used for STI
    }

    def __init__(self, first_name, last_name, email, password, role=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role": self.role
        }

# Client Model
class Client(User):
    """ Modèle pour les clients. """
    __mapper_args__ = {
        'polymorphic_identity': 'Client',  # Identity for Client
    }

# Coach Model
class Coach(User):
    """ Modèle pour les coachs. """
    __mapper_args__ = {
        'polymorphic_identity': 'Coach',  # Identity for Coach
    }

