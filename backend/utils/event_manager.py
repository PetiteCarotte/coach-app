""" Gestionnaire d'événements pour implémenter le pattern Observer. """
class EventManager:
    """Gestionnaire d'événements pour implémenter le pattern Observer (Singleton)."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EventManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_observers'):
            self._observers = {}  # Initialisé une seule fois pour l'instance unique

    def subscribe(self, event_type, observer):
        """Abonner un observateur à un type d'événement."""
        if event_type not in self._observers:
            self._observers[event_type] = []
        self._observers[event_type].append(observer)

    def unsubscribe(self, event_type, observer):
        """Désabonner un observateur d'un type d'événement."""
        if event_type in self._observers:
            self._observers[event_type].remove(observer)

    def notify(self, event_type, data):
        """Notifier tous les observateurs d'un type d'événement."""
        if event_type in self._observers:
            for observer in self._observers[event_type]:
                observer.update(event_type, data)
