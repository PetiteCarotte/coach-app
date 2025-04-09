from utils.db import app, db
import routes
from routes import routes
from models import Program
from utils.insert_data import insert_default_programs  
from utils.insert_data import insert_default_slots

routes(app)
if __name__ == '__main__':
    # Initialisation de la base de données et insertion des programmes par défaut
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
        insert_default_programs()
        insert_default_slots()

    app.run(debug=True)