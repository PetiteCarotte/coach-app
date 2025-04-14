""" Observateur pour journaliser les événements de réservation. """

# pylint: disable=import-error, too-few-public-methods

import logging
from observers.observer_interface import Observer

class LoggingObserver(Observer):
    """Observateur pour journaliser les événements."""

    def __init__(self):
        """Initialiser l'observateur de journalisation."""
        # Configurer le fichier de logs
        logging.basicConfig(
            filename="logs/reservation_events.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def update(self, event_type, data):
        """Journaliser les événements."""
        if event_type == "reservation_created":
            message = (
                f"Reservation {data['reservation_id']} creee pour le client "
                f"{data['client_id']}."
            )
            logging.info(message)
            print(f"LOG: {message}")
        elif event_type == "reservation_cancelled":
            message = (
                f"Reservation {data['reservation_id']} annulee pour le client "
                f"{data['client_id']}."
            )
            logging.info(message)
            print(f"LOG: {message}")
