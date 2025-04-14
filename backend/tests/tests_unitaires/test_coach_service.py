""" Test unitaire pour le service de coachs """

# pylint: disable=import-error, unused-argument

from unittest.mock import patch, MagicMock
from services.coach_service import get_coaches_service

def test_get_coaches_service(app_context):
    """ Tester la récupération des coachs """
    with patch("services.coach_service.Coach.query") as mock_query:
        mock_query.all.return_value = [MagicMock(id=1, first_name="John", last_name="Doe")]
        coaches = get_coaches_service()
        assert len(coaches) == 1
