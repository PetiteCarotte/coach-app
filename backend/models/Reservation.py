from utils.db import db

class Reservation(db.Model):
    """Modèle pour les réservations."""

    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('slots.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('pending', 'confirmed', 'cancelled', name='reservation_status'), default='pending', nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    client = db.relationship("Client", foreign_keys=[client_id])
    coach = db.relationship("Coach", foreign_keys=[coach_id])
    program = db.relationship("Program", back_populates="reservations")
    slot = db.relationship("Slot", back_populates="reservations")
