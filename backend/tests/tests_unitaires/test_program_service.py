""" Test unitaire pour le service de programmes """

# pylint: disable=import-error, unused-argument

from unittest.mock import patch, MagicMock
from services.program_service import get_programs_service

@patch("services.program_service.Program.query")
def test_get_programs_service(mock_query, app_context):
    """ Tester la récupération des programmes """
    program1 = MagicMock()
    program1.name = "Objectif Minceur"
    program2 = MagicMock()
    program2.name = "Muscle & Force"
    program3 = MagicMock()
    program3.name = "Bilan Fitness"

    mock_query.all.return_value = [program1, program2, program3]

    programs = get_programs_service()

    expected_names = {"Objectif Minceur", "Muscle & Force", "Bilan Fitness"}
    program_names = {program.name for program in programs}

    assert program_names == expected_names
    assert len(programs) == 3
