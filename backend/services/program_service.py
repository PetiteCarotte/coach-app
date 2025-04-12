# program_service.py

from models.Program import Program

def get_programs_service():
    """Récupérer la liste des programmes."""
    
    try:
        programs = Program.query.all()
        return programs
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération des programmes : {str(e)}")


