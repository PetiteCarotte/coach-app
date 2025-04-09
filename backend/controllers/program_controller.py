from models import Program

def get_all_programs():
    programs = Program.query.all()
    return [{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'duration_minutes': p.duration_minutes
    } for p in programs]
