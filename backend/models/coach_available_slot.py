"""Définit le modèle des créneaux disponibles pour les coachs."""

#pylint: disable=too-few-public-methods

from utils.db import db

class CoachAvailableSlot(db.Model):
    """Modèle pour les créneaux disponibles des coachs."""

    __tablename__ = 'coach_available_slots'

    id = db.Column(db.Integer, primary_key=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('slots.id'), nullable=False)

    coach = db.relationship("Coach", backref="available_slots")
    slot = db.relationship("Slot", back_populates="coach_availabilities")
