from .auth import auth_router
from .ai import ai_router
from .roadmap import roadmap_router
from .user import user_router
from .attachment import attachment_router


def register_blueprints(app):
    app.register_blueprint(auth_router, url_prefix="/auth")
    app.register_blueprint(ai_router, url_prefix="/ai")
    app.register_blueprint(roadmap_router, url_prefix="/roadmap")
    app.register_blueprint(user_router, url_prefix="/user")
    app.register_blueprint(attachment_router, url_prefix="/attachment")
