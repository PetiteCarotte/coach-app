""" Observateur pour envoyer des emails. """

# pylint: disable=import-error, too-few-public-methods

from observers.observer_interface import Observer
from adapters.email_adapter import SMTPAdapter

class EmailObserver(Observer):
    """Observateur pour envoyer des emails."""

    def __init__(self, email_service=None):
        self.email_service = email_service or SMTPAdapter() # Utiliser SMTP par défaut

    def update(self, event_type, data):
        """Envoyer un email en fonction de l'événement."""
        if event_type == "reservation_created":
            self.email_service.send_email(
                to=data['client_email'],
                subject="Confirmation de réservation",
                body=f"Votre réservation {data['reservation_id']} a été confirmée."
            )
        elif event_type == "reservation_cancelled":
            self.email_service.send_email(
                to=data['client_email'],
                subject="Annulation de réservation",
                body=f"Votre réservation {data['reservation_id']} a été annulée."
            )
