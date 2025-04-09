from utils.db import db

# Association Coach ↔ Slot
class CoachAvailableSlot(db.Model):
    __tablename__ = 'coach_available_slots'

    id = db.Column(db.Integer, primary_key=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('slots.id'), nullable=False)

    coach = db.relationship("Coach", backref="available_slots")
    slot = db.relationship("Slot", back_populates="coach_availabilities")
