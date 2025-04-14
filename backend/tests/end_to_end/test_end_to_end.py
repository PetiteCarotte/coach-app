""" Test end-to-end pour le flux utilisateur complet """

# pylint: disable=import-error, import-outside-toplevel

from app import app

def test_end_to_end_user_flow(client):
    """ Tester le flux utilisateur complet : inscription, connexion, réservation, annulation """
    # Étape 1 : Inscrire un client
    client_response = client.post('/api/register', json={
        "firstName": "Alice",
        "lastName": "Smith",
        "email": "alice.smith@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Client"
    })
    assert client_response.status_code == 201
    assert "Inscription réussie" in client_response.json["message"]

    # Étape 2 : Se connecter en tant que client
    login_response = client.post('/api/login', json={
        "email": "alice.smith@example.com",
        "password": "password123"
    })
    assert login_response.status_code == 200
    assert "Connexion réussie" in login_response.json["message"]
    client_token = login_response.json["token"]

    # Étape 3 : Inscrire un coach
    coach_response = client.post('/api/register', json={
        "firstName": "Bob",
        "lastName": "Coach",
        "email": "bob.coach@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Coach"
    })
    assert coach_response.status_code == 201
    assert "Inscription réussie" in coach_response.json["message"]

    # Étape 4 : Récupérer l'ID du coach
    with app.app_context():
        from models.user import Coach
        coach = Coach.query.filter_by(email="bob.coach@example.com").first()
        coach_id = coach.id

    # Étape 5 : Créer une réservation
    reservation_response = client.post('/api/reservations', json={
        "coach_id": coach_id,
        "program_id": 1,
        "slot_id": 1,
        "date": "2023-12-01"
    }, headers={"Authorization": f"Bearer {client_token}"})
    assert reservation_response.status_code == 201
    assert "Réservation créée avec succès" in reservation_response.json["message"]
