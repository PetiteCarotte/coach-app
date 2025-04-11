from models.User import Client, Coach

class UserFactory:
    """ Factory pour créer des instances User basées sur le rôle. """
    user_creators = {
        "Client": lambda first_name, last_name, email, password: Client(first_name, last_name, email, password, role="Client"),
        "Coach": lambda first_name, last_name, email, password: Coach(first_name, last_name, email, password, role="Coach"),
    }

    @staticmethod
    def create_user(role, first_name, last_name, email, password):
        """ Crée un utilisateur basé sur le rôle spécifié. """
        if role not in UserFactory.user_creators:
            raise ValueError(f"Role invalide: {role}")
        return UserFactory.user_creators[role](first_name, last_name, email, password)
