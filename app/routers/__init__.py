from .auth import auth_router
from .user import user_router


def register_blueprints(app):
    app.register_blueprint(auth_router, url_prefix="/auth")
    app.register_blueprint(user_router, url_prefix="/user")
