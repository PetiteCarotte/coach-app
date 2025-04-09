from utils.db import db

# Slot Model (créneaux horaires génériques)
class Slot(db.Model):
    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    coach_availabilities = db.relationship("CoachAvailableSlot", back_populates="slot")
    reservations = db.relationship("Reservation", back_populates="slot")
