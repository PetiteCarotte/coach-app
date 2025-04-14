""" Interface pour les observateurs dans le modèle Observer."""

# pylint: disable=too-few-public-methods, unnecessary-pass

from abc import ABC, abstractmethod

class Observer(ABC):
    """Interface pour les observateurs."""

    @abstractmethod
    def update(self, event_type, data):
        """Méthode appelée pour notifier l'observateur d'un événement."""
        pass
