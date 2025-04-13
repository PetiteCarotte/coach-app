from utils.db import app, db
import routes
from routes import routes
from models import Program
from utils.insert_data import insert_default_programs  
from utils.insert_data import insert_default_slots
from factories.user_factory import UserFactory
from utils.event_manager import EventManager
from observers.email_observer import EmailObserver
from observers.logging_observer import LoggingObserver

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