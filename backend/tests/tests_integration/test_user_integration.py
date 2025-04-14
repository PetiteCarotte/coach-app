""" Tests d'intégration pour les utilisateurs. """

# pylint: disable=import-error, import-outside-toplevel

def test_user_registration(client):
    """ Tester l'inscription d'un utilisateur. """
    # Tu envoies une requête pour t'assurer que l'inscription fonctionne
    response = client.post('/api/register', json={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Client"
    })
    assert response.status_code == 201
    assert "Inscription réussie !" in response.json["message"]

def test_user_login(client):
    """ Tester la connexion d'un utilisateur. """
    client.post('/api/register', json={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Client"
    })
    response = client.post('/api/login', json={
        "email": "john.doe@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "Connexion réussie" in response.json["message"]
    assert "token" in response.json

def test_get_my_reservations(client):
    """ Tester la récupération des réservations de l'utilisateur. """
    client.post('/api/register', json={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "confirmPassword": "password123",
        "role": "Client"
    })
    login_response = client.post('/api/login', json={
        "email": "john.doe@example.com",
        "password": "password123"
    })
    token = login_response.json["token"]
    response = client.get('/api/my_reservations', headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_coach_registration(client):
    """ Tester l'inscription d'un coach. """
    response = client.post('/api/register', json={
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "password": "securepassword",
        "confirmPassword": "securepassword",
        "role": "Coach"
    })
    assert response.status_code == 201
    assert "Inscription réussie !" in response.json["message"]

def test_coach_login(client):
    """ Tester la connexion d'un coach. """
    client.post('/api/register', json={
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "password": "securepassword",
        "confirmPassword": "securepassword",
        "role": "Coach"
    })
    response = client.post('/api/login', json={
        "email": "jane.smith@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert "Connexion réussie" in response.json["message"]
    assert "token" in response.json
