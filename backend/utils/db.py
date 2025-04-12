from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    """Singleton pour la gestion de la base de données."""

    _instance = None

    def __new__(cls):
        """Implémentation du Singleton."""

        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.init_app()
        return cls._instance

    def init_app(self):
        """Initialisation de l'application Flask et de la base de données."""
        
        self.app = Flask(__name__)
        self.app.secret_key = 'supersecretkey'  # Clé secrète pour les sessions
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)

# Utilisation du Singleton
db_manager = DatabaseManager()
app = db_manager.app
db = db_manager.db
