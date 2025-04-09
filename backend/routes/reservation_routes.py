from flask import Blueprint, request, jsonify
from models.Slot import Slot
from models.Reservation import Reservation
from models.CoachAvailableSlot import CoachAvailableSlot
from utils.db import db
from datetime import datetime
from sqlalchemy import and_

reservation_routes = Blueprint('reservation_routes', __name__)

# Obtenir les créneaux disponibles pour un coach à une date donnée
@reservation_routes.route('/available_slots', methods=['GET'])
def get_available_slots():
    coach_id = request.args.get('coach_id', type=int)
    date_str = request.args.get('date', type=str)

    if not coach_id or not date_str:
        return jsonify({"error": "Missing coach_id or date parameter"}), 400

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

        return jsonify(available_slots), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Créer une réservation
@reservation_routes.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    required_fields = ['coach_id', 'program_id', 'slot_id', 'date']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Champs manquants'}), 400

    try:
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()

        # Vérifier si le coach a déjà une réservation pour ce créneau
        existing_reservation = Reservation.query.filter_by(
            coach_id=data['coach_id'],
            slot_id=data['slot_id'],
            date=date_obj
        ).first()

        if existing_reservation:
            return jsonify({'error': 'Le coach a déjà une réservation pour ce créneau.'}), 400

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
        return jsonify({'message': 'Réservation créée avec succès'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
