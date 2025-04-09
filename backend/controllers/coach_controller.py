from models import Coach

def get_all_coaches():
    coaches = Coach.query.all()
    return [coach.to_dict() for coach in coaches]
