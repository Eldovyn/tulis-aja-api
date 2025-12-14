from flask import Blueprint
from ..controllers import AttachmentController

attachment_router = Blueprint("attachment_router", __name__)
attachment_controller = AttachmentController()


@attachment_router.get("/mascot/<string:level>")
def get_mascot(level):
    return attachment_controller.get_mascot(level)
