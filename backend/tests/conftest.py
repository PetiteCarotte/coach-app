# conftest.py (à la racine de tests/)
import pytest
from app import app
from app import db
from sqlalchemy.orm import scoped_session, sessionmaker

@pytest.fixture(scope="module")
def app_context():
    """Fixture pour le contexte de l'application."""
    with app.app_context():
        yield

@pytest.fixture(scope="function")
def client():
    """Fixture pour isoler les tests avec rollback automatique à la fin de chaque test."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/mondb'

    with app.app_context():
        # Connexion et début de transaction
        connection = db.engine.connect()
        transaction = connection.begin()

        # Nouvelle session liée à la transaction
        session_factory = sessionmaker(bind=connection)
        session = scoped_session(session_factory)

        # Remplace la session globale par celle-ci
        db.session = session

        with app.test_client() as client:
            yield client

        # Cleanup : rollback et fermeture de session
        transaction.rollback()
        connection.close()
        session.remove()
