from flask import Blueprint, request
from ..utils import jwt_required
from ..controllers import NoteController

note_router = Blueprint("note_router", __name__)
note_controller = NoteController()


@note_router.post("/")
@jwt_required()
async def create_note():
    user = request.user
    json_data = request.json
    title = json_data.get("title", "")
    content = json_data.get("content", "")
    return await note_controller.create_note(user, title, content)


@note_router.get("/")
@jwt_required()
async def get_all_notes():
    user = request.user
    return await note_controller.get_all_notes(user)
