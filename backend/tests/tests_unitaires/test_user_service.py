""" Tests unitaires pour le service utilisateur. """


# pylint: disable=import-error, unused-argument, redefined-outer-name

from unittest.mock import patch, MagicMock
import pytest
from services.user_service import register_new_user, authenticate_user, get_reservations_for_client

@pytest.fixture
def mock_user():
    """ Fixture pour un utilisateur fictif """
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "confirm_password": "password123",
        "role": "Client"
    }

@patch("services.user_service.User.query")
@patch("services.user_service.db")
def test_register_new_user_success(mock_db, mock_query, mock_user, app_context):
    """ Tester l'inscription d'un nouvel utilisateur """
    mock_query.filter_by.return_value.first.return_value = None
    response, status = register_new_user(**mock_user)
    assert status == 201
    assert "Inscription réussie" in response["message"]

@patch("services.user_service.User.query")
def test_register_new_user_email_exists(mock_query, mock_user, app_context):
    """ Tester l'inscription avec un email déjà utilisé """
    mock_query.filter_by.return_value.first.return_value = MagicMock()
    response, status = register_new_user(**mock_user)
    assert status == 400
    assert "Cet email est déjà utilisé" in response["error"]

def test_register_new_user_password_mismatch(mock_user):
    """ Tester l'inscription avec des mots de passe non concordants """
    mock_user["confirm_password"] = "wrongpassword"
    response, status = register_new_user(**mock_user)
    assert status == 400
    assert "Les mots de passe ne correspondent pas" in response["error"]

# Test pour l'authentification avec succès
@patch("services.user_service.User.query")
def test_authenticate_user_success(mock_query, app_context):
    """ Tester l'authentification d'un utilisateur """
    # Créez un mock d'utilisateur avec des attributs JSON sérialisables
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = "john.doe@example.com"
    mock_user.check_password.return_value = True  # Simule la méthode check_password

    # Simulez la recherche de l'utilisateur dans la base de données
    mock_query.filter_by.return_value.first.return_value = mock_user

    # Appelez la fonction d'authentification
    user, token = authenticate_user("john.doe@example.com", "password123")

    # Assurez-vous que l'utilisateur et le token sont renvoyés
    assert user is not None
    assert token is not None

@patch("services.user_service.User.query")
def test_authenticate_user_invalid_credentials(mock_query, app_context):
    """ Tester l'authentification avec des identifiants invalides """
    mock_query.filter_by.return_value.first.return_value = None
    user, token = authenticate_user("john.doe@example.com", "wrongpassword")
    assert user is None
    assert token is None

@patch("services.user_service.ClientStrategy.view_reservations")
def test_get_reservations_for_client(mock_view_reservations):
    """ Tester la récupération des réservations pour un client """
    mock_view_reservations.return_value = [{"id": 1, "program_name": "Test Program"}]
    reservations = get_reservations_for_client(1)
    assert len(reservations) == 1
    assert reservations[0]["program_name"] == "Test Program"
