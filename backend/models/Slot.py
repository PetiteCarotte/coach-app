"""Définit le modèle des créneaux horaires."""

# pylint: disable=too-few-public-methods

from utils.db import db

class Slot(db.Model):
    """Modèle pour les créneaux horaires."""

    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    coach_availabilities = db.relationship("CoachAvailableSlot", back_populates="slot")
    reservations = db.relationship("Reservation", back_populates="slot")
