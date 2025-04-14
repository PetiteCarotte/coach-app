""" Tests unitaires pour le service de reservation. """

# pylint: disable=import-error, unused-argument

from datetime import time
from unittest.mock import patch, MagicMock
from services.reservation_service import (
    get_available_slots_service,
    create_reservation_service,
    cancel_reservation_service,
)

@patch("services.reservation_service.Slot.query")
@patch("services.reservation_service.Reservation.query")
def test_get_available_slots_service(mock_reservation_query, mock_slot_query, app_context):
    """ Tester la récupération des créneaux disponibles pour un coach """
    # Convertir la date en chaîne de caractères
    test_date = "2023-12-01"

    # Simuler la réponse de la base de données pour les créneaux
    mock_slot_query.all.return_value = [MagicMock(id=1, start_time=time(8, 0), end_time=time(9, 0))]
    mock_reservation_query.filter_by.return_value.first.return_value = None

    # Appeler la fonction avec la chaîne de caractères
    slots = get_available_slots_service(1, test_date)

    # Vérifications
    assert len(slots) == 1
    assert slots[0]["is_reserved"] is False
    assert slots[0]["start_time"] == "08:00"
    assert slots[0]["end_time"] == "09:00"

@patch("services.reservation_service.Reservation.query")
@patch("services.reservation_service.db")
def test_create_reservation_service_success(mock_db, mock_reservation_query, app_context):
    """ Tester la création d'une réservation """
    mock_reservation_query.filter_by.return_value.first.return_value = None
    data = {"coach_id": 1, "program_id": 1, "slot_id": 1, "date": "2023-12-01"}
    token = "valid.jwt.token"
    with patch("services.reservation_service.jwt.decode", return_value={"user_id": 1}):
        response = create_reservation_service(data, token)
        assert "Réservation créée avec succès" in response["message"]

@patch("services.reservation_service.ClientStrategy.cancel_reservation")
@patch("services.reservation_service.db")
def test_cancel_reservation_service_success(mock_db, mock_cancel_reservation, app_context):
    """ Tester l'annulation d'une réservation """
    mock_cancel_reservation.return_value = {"client_id": 1, "client_email": "test@example.com"}
    response = cancel_reservation_service(1)
    assert "Réservation annulée avec succès" in response["message"]
