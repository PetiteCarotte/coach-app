from abc import ABC, abstractmethod

class Observer(ABC):
    """Interface pour les observateurs."""

    @abstractmethod
    def update(self, event_type, data):
        """Méthode appelée pour notifier l'observateur d'un événement."""
        pass
