# reservation_service.py

from models.Slot import Slot
from models.Reservation import Reservation
from models.CoachAvailableSlot import CoachAvailableSlot
from utils.db import db
from datetime import datetime

def get_available_slots_service(coach_id, date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        slots = Slot.query.all()

        available_slots = []
        for slot in slots:
            is_reserved = Reservation.query.filter_by(
                coach_id=coach_id,
                slot_id=slot.id,
                date=date_obj
            ).first() is not None

            available_slots.append({
                'id': slot.id,
                'start_time': slot.start_time.strftime('%H:%M'),
                'end_time': slot.end_time.strftime('%H:%M'),
                'is_reserved': is_reserved
            })

        return available_slots

    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération des créneaux disponibles : {str(e)}")

def create_reservation_service(data):
    try:
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()

        # Vérifier si le coach a déjà une réservation pour ce créneau
        existing_reservation = Reservation.query.filter_by(
            coach_id=data['coach_id'],
            slot_id=data['slot_id'],
            date=date_obj
        ).first()

        if existing_reservation:
            return {'error': 'Le coach a déjà une réservation pour ce créneau.'}

        # Créer la réservation si aucune réservation existante n'est trouvée
        reservation = Reservation(
            client_id=1,  # À adapter avec un vrai user_id / JWT
            coach_id=data['coach_id'],
            program_id=data['program_id'],
            slot_id=data['slot_id'],
            date=date_obj
        )
        db.session.add(reservation)
        db.session.commit()
        return {'message': 'Réservation créée avec succès'}

    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Erreur lors de la création de la réservation : {str(e)}")

