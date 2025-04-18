""" Service pour la gestion des coachs. """

# pylint: disable=raise-missing-from

from models.user import Coach

def get_coaches_service():
    """Récupérer la liste des coachs."""

    try:
        coaches = Coach.query.all()
        return coaches
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération des coachs : {str(e)}")
