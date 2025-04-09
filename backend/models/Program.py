from utils.db import db

# Program Model
class Program(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration_minutes = db.Column(db.Integer, nullable=False)

    reservations = db.relationship("Reservation", back_populates="program")