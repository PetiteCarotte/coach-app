from observers.observer_interface import Observer

class EmailObserver(Observer):
    """Observateur pour envoyer des emails."""

    def update(self, event_type, data):
        """Envoyer un email en fonction de l'événement."""
        
        if event_type == "reservation_created":
            print(f"Envoi d'un email de confirmation a {data['client_email']} pour la reservation {data['reservation_id']}.")
        elif event_type == "reservation_cancelled":
            print(f"Envoi d'un email d'annulation a {data['client_email']} pour la reservation {data['reservation_id']}.")
