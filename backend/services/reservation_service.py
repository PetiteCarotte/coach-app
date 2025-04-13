# reservation_service.py

from models.Slot import Slot
from models.Reservation import Reservation
from models.CoachAvailableSlot import CoachAvailableSlot
from models.User import User 
from utils.db import db
from utils.event_manager import EventManager
from datetime import datetime
import jwt
from strategies.user_strategies import ClientStrategy

SECRET_KEY = 'supersecretkey'

# Utiliser l'instance Singleton d'EventManager
event_manager = EventManager()

def get_available_slots_service(coach_id, date_str):
    """Récupérer les créneaux disponibles pour un coach donné à une date spécifique."""

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

def create_reservation_service(data, token):
    """Créer une réservation pour un client."""
    
    try:
        # Décoder le token JWT pour obtenir le client_id
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        client_id = decoded.get('user_id')

        # Récupérer l'email du client depuis la table User
        client = User.query.get(client_id)
        if not client:
            raise ValueError("Client introuvable.")

        date_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()

        # Vérifier si le coach a déjà une réservation pour ce créneau
        existing_reservation = Reservation.query.filter_by(
            coach_id=data['coach_id'],
            slot_id=data['slot_id'],
            date=date_obj
        ).first()

        if existing_reservation:
            return {'error': 'Le coach a déjà une réservation pour ce créneau.'}

        # Créer la réservation avec le client_id extrait du token
        reservation = Reservation(
            client_id=client_id,
            coach_id=data['coach_id'],
            program_id=data['program_id'],
            slot_id=data['slot_id'],
            date=date_obj
        )
        db.session.add(reservation)
        db.session.commit()

        # Notifier les observateurs
        event_manager.notify("reservation_created", {
            "reservation_id": reservation.id,
            "client_id": client_id,
            "client_email": client.email,  # Utiliser l'email récupéré depuis la table User
        })

        return {'message': 'Réservation créée avec succès'}

    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Erreur lors de la création de la réservation : {str(e)}")

def cancel_reservation_service(reservation_id):
    """Annuler une réservation."""

    try:
        # Utiliser la stratégie pour annuler la réservation
        result = ClientStrategy.cancel_reservation(reservation_id)
        db.session.commit()

        # Notifier les observateurs
        event_manager.notify("reservation_cancelled", {
            "reservation_id": reservation_id,
            "client_id": result['client_id'],
            "client_email": result['client_email'],
        })

        return {'message': 'Réservation annulée avec succès'}
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Erreur lors de l'annulation de la réservation : {str(e)}")

