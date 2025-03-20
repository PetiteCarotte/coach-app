from utils.db import app, db
import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
    app.run(debug=True)