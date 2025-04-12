from .user_routes import user_routes
from .coach_routes import coach_routes
from .program_routes import program_routes
from .reservation_routes import reservation_routes

def routes(app):
    """ Initialisation des routes de l'application Flask."""
    
    app.register_blueprint(user_routes, url_prefix='/api')
    app.register_blueprint(coach_routes, url_prefix='/api')
    app.register_blueprint(program_routes, url_prefix='/api')
    app.register_blueprint(reservation_routes, url_prefix='/api')
