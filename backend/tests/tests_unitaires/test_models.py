""" Tests unitaires pour les modèles. """

# pylint: disable=import-error

from datetime import time, date
from models.user import User, Client, Coach
from models.slot import Slot
from models.reservation import Reservation
from models.program import Program

def test_user_model():
    """Tester la création d'un utilisateur générique."""
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        password="password123",
        role="Client"
    )
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.check_password("password123")
    assert user.role == "Client"

def test_client_model():
    """Tester la création d'un client."""
    client = Client(
        first_name="Jane",
        last_name="Doe",
        email="jane.doe@example.com",
        password="password123",
        role="Client"
    )
    assert client.role == "Client"
    assert client.email == "jane.doe@example.com"

def test_coach_model():
    """Tester la création d'un coach."""
    coach = Coach(
        first_name="Bob",
        last_name="Smith",
        email="bob.smith@example.com",
        password="password123",
        role="Coach"
    )
    assert coach.role == "Coach"
    assert coach.first_name == "Bob"

def test_slot_model():
    """Tester la création d'un créneau horaire."""
    slot = Slot(start_time=time(8, 0), end_time=time(9, 0))
    assert slot.start_time == time(8, 0)
    assert slot.end_time == time(9, 0)

def test_reservation_model():
    """Tester la création d'une réservation."""
    reservation = Reservation(
        client_id=1,
        coach_id=2,
        program_id=3,
        slot_id=4,
        date=date(2023, 12, 1),
        status="pending"
    )
    assert reservation.date == date(2023, 12, 1)
    assert reservation.client_id == 1
    assert reservation.coach_id == 2
    assert reservation.status == "pending"

def test_program_model():
    """Tester la création d'un programme."""
    program = Program(name="Test Program", description="Description", duration_minutes=60)
    assert program.name == "Test Program"
    assert program.duration_minutes == 60
