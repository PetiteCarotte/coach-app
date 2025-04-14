""" Tests d'intégration pour les réservations."""

# pylint: disable=import-error, import-outside-toplevel

from app import app

def create_coach_and_get_id(client):
    """Créer un coach et récupérer son ID directement depuis la base de données."""
    client.post('/api/register', json={
        "firstName": "Bob",
        "lastName": "Coach",
        "email": "bob.coach@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Coach"
    })
    with app.app_context():
        from models.user import Coach
        coach = Coach.query.filter_by(email="bob.coach@example.com").first()
        return coach.id

def test_create_reservation(client):
    """Tester la création d'une réservation."""
    # Créer un coach et récupérer son ID
    coach_id = create_coach_and_get_id(client)

    # Créer un utilisateur client
    client.post('/api/register', json={
        "firstName": "Alice",
        "lastName": "Smith",
        "email": "alice.smith@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Client"
    })
    login_response = client.post('/api/login', json={
        "email": "alice.smith@example.com",
        "password": "password123"
    })
    token = login_response.json["token"]

    # Créer une réservation avec l'ID du coach
    response = client.post('/api/reservations', json={
        "coach_id": coach_id,
        "program_id": 1,
        "slot_id": 1,
        "date": "2023-12-01"
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert "Réservation créée avec succès" in response.json["message"]

def test_get_available_slots(client):
    """Tester la récupération des créneaux disponibles pour un coach."""
    # Créer un coach et récupérer son ID
    coach_id = create_coach_and_get_id(client)

    # Vérifier les créneaux disponibles pour le coach
    response = client.get(f'/api/available_slots?coach_id={coach_id}&date=2023-12-01')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert "start_time" in response.json[0]
    assert "end_time" in response.json[0]
