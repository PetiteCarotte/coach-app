"""Définit le modèle de programme d'entraînement."""

# pylint: disable=too-few-public-methods

from utils.db import db

class Program(db.Model):
    """Modèle pour les programmes d'entraînement."""

    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration_minutes = db.Column(db.Integer, nullable=False)

    reservations = db.relationship("Reservation", back_populates="program")
