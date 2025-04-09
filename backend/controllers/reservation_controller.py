from models import CoachAvailableSlot, Reservation
from datetime import datetime
from utils.db import db

def get_available_slots(coach_id, date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return {'error': 'Format de date invalide. Utiliser YYYY-MM-DD'}, 400

    all_slots = CoachAvailableSlot.query.filter_by(coach_id=coach_id).all()
    reserved_ids = {slot_id for (slot_id,) in db.session.query(Reservation.slot_id).filter_by(coach_id=coach_id, date=date).all()}
    available = [s.slot for s in all_slots if s.slot.id not in reserved_ids]

    return [{
        'id': s.id,
        'start_time': s.start_time.strftime('%H:%M'),
        'end_time': s.end_time.strftime('%H:%M')
    } for s in available], 200

def create_reservation(client_id, data):
    from models import Reservation

    try:
        date = datetime.strptime(data.get('date'), '%Y-%m-%d').date()
    except ValueError:
        return {'error': 'Format de date invalide. Utiliser YYYY-MM-DD'}, 400

    coach_id = data.get('coach_id')
    program_id = data.get('program_id')
    slot_id = data.get('slot_id')

    if not all([client_id, coach_id, program_id, slot_id]):
        return {'error': 'Tous les champs sont requis'}, 400

    existing = Reservation.query.filter_by(coach_id=coach_id, slot_id=slot_id, date=date).first()
    if existing:
        return {'error': 'Ce créneau est déjà réservé'}, 409

    reservation = Reservation(
        client_id=client_id,
        coach_id=coach_id,
        program_id=program_id,
        slot_id=slot_id,
        date=date,
        status='confirmed'
    )
    db.session.add(reservation)
    db.session.commit()
    return {'message': 'Réservation confirmée !'}, 201
