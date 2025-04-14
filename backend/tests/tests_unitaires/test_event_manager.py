""" Tests unitaires pour le module EventManager. """

# pylint: disable=import-error

from unittest.mock import MagicMock
from utils.event_manager import EventManager

def test_event_manager_subscribe_and_notify():
    """ Test de l'abonnement et de la notification d'un événement. """
    event_manager = EventManager()
    observer = MagicMock()
    event_manager.subscribe("test_event", observer)
    event_manager.notify("test_event", {"key": "value"})
    observer.update.assert_called_once_with("test_event", {"key": "value"})

def test_event_manager_unsubscribe():
    """ Test de la désinscription d'un événement. """
    event_manager = EventManager()
    observer = MagicMock()
    event_manager.subscribe("test_event", observer)
    event_manager.unsubscribe("test_event", observer)
    event_manager.notify("test_event", {"key": "value"})
    observer.update.assert_not_called()
