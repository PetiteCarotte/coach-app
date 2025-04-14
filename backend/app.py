""" Point d'entrée de l'application Flask."""

from utils.db import app, db
from utils.insert_data import insert_default_programs, insert_default_slots
from utils.event_manager import EventManager
from observers.email_observer import EmailObserver
from observers.logging_observer import LoggingObserver
from routes import routes

# Initialisation de l'EventManager (Singleton)
event_manager = EventManager()

routes(app)
if __name__ == '__main__':
    # Initialisation de la base de données et insertion des programmes par défaut
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
        insert_default_programs()
        insert_default_slots()

    # Enregistrer les observateurs
    event_manager.subscribe("reservation_created", EmailObserver())
    event_manager.subscribe("reservation_created", LoggingObserver())
    event_manager.subscribe("reservation_cancelled", EmailObserver())
    event_manager.subscribe("reservation_cancelled", LoggingObserver())

    app.run(debug=True)
