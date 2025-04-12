from utils.db import db
from datetime import datetime, timedelta
from models.Slot import Slot
from models.Program import Program

def insert_default_programs():
    """Insérer des programmes par défaut dans la base de données."""

    # Vérifie si des programmes existent déjà dans la base
    if Program.query.count() == 0:
        # Insérer les programmes par défaut
        programs = [
            Program(name='Objectif Minceur', duration_minutes='60', description='Un programme conçu pour brûler les graisses et affiner votre corps de manière saine et durable.'),
            Program(name='Muscle & Force', duration_minutes='60', description='Un programme intensif pour augmenter votre masse musculaire et renforcer votre corps.'),
            Program(name='Bilan Fitness', duration_minutes='60', description='Une évaluation complète de votre condition physique pour définir un plan d\'action sur-mesure.')
        ]
        
        db.session.add_all(programs)
        db.session.commit()
        print("Programmes par défaut insérés avec succès.")
    else:
        print("Les programmes existent déjà dans la base de données.")


def insert_default_slots():
    """Insérer des créneaux horaires par défaut dans la base de données."""
    
    # Vérifie si des créneaux existent déjà dans la base de données
    if Slot.query.count() == 0:
        # Définir l'heure de début (8h00) et l'heure de fin (18h00)
        start_time = datetime.strptime("08:00", "%H:%M")
        end_time = datetime.strptime("18:00", "%H:%M")
        
        # Liste pour stocker les créneaux à insérer
        slots = []

        # Générer des créneaux horaires entre 8h et 17h
        while start_time < end_time:
            next_time = start_time + timedelta(hours=1)
            # Créer un créneau avec start_time et next_time (end_time)
            slots.append(Slot(start_time=start_time.time(), end_time=next_time.time()))
            start_time = next_time

        # Insérer les créneaux dans la base de données
        db.session.add_all(slots)
        db.session.commit()
        print("Créneaux horaires par défaut insérés avec succès.")
    else:
        print("Les créneaux horaires existent déjà dans la base de données.")

