""" Module de gestion de la base de données avec Flask et SQLAlchemy. """

# pylint: disable=attribute-defined-outside-init

import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
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
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = (
            f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)

# Utilisation du Singleton
db_manager = DatabaseManager()
app = db_manager.app
db = db_manager.db
