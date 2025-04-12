from models.User import Client, Coach
from strategies.user_strategies import ClientStrategy, CoachStrategy

class UserFactory:
    """Factory combinée avec des stratégies pour créer des utilisateurs."""

    user_creators = {
        "Client": lambda first_name, last_name, email, password: Client(first_name, last_name, email, password, role="Client"),
        "Coach": lambda first_name, last_name, email, password: Coach(first_name, last_name, email, password, role="Coach"),
    }

    user_strategies = {
        "Client": ClientStrategy,
        "Coach": CoachStrategy,
    }

    @staticmethod
    def create_user(role, first_name, last_name, email, password):
        """Créer un utilisateur en fonction du rôle."""

        if role not in UserFactory.user_creators:
            raise ValueError(f"Role invalide: {role}")
        
        # Créer l'utilisateur
        user = UserFactory.user_creators[role](first_name, last_name, email, password)
        
        # Associer la stratégie au rôle
        strategy = UserFactory.user_strategies[role]
        user.strategy = strategy  # Injecter la stratégie dans l'utilisateur
        
        return user
