from models.Reservation import Reservation

class ClientStrategy:
    """Stratégie pour les clients."""

    @staticmethod
    def perform_action():
        """Action spécifique au client."""

        return "Le client peut réserver un programme et consulter ses réservations."

    @staticmethod
    def view_reservations(client_id):
        """Afficher les réservations du client."""

        # Récupérer les réservations d'un client depuis la base de données
        reservations = Reservation.query.filter_by(client_id=client_id).all()

        formatted_reservations = [
            {
                "id": res.id,
                "program_name": res.program.name,
                "coach_name": f"{res.coach.first_name} {res.coach.last_name}",
                "date": res.date.strftime('%Y-%m-%d'),
                "start_time": res.slot.start_time.strftime('%H:%M'),
                "end_time": res.slot.end_time.strftime('%H:%M'),
            }
            for res in reservations
        ]
        return formatted_reservations

    @staticmethod
    def cancel_reservation(reservation_id):
        """Annuler une réservation."""

        return f"Réservation avec l'ID {reservation_id} annulée pour le client."


class CoachStrategy:
    """Stratégie pour les coachs."""

    @staticmethod
    def perform_action():
        """Action spécifique au coach."""

        return "Le coach peut gérer ses créneaux disponibles et consulter ses sessions."

    @staticmethod
    def manage_slots(coach_id):
        """Gérer les créneaux disponibles du coach."""

        return f"Gestion des créneaux pour le coach avec l'ID {coach_id}."

    @staticmethod
    def view_sessions(coach_id):
        """Afficher les sessions du coach."""

        return f"Affichage des sessions pour le coach avec l'ID {coach_id}."
