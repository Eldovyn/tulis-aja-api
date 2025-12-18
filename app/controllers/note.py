from ..databases import NoteDatabase
from ..serializers import NoteSerializer
from flask import jsonify
from ..utils import NoteAI, NoteSummaryParseError


class NoteController:
    def __init__(self):
        self.note_serializer = NoteSerializer()
        self.note_ai = NoteAI()

    async def update_note(self, user, note_id, title, content):
        note_ai = self.note_ai.summarize_note(content)
        note_data = await NoteDatabase.update(
            category="update_note_by_user_id",
            note_id=note_id,
            user_id=f"{user.id}",
            title=title,
            content=content,
            summary=note_ai["summary"],
            tags=note_ai["bullets"],
        )
        note_serializer = self.note_serializer.serialize(note_data)
        return (
            jsonify(
                {
                    "message": "note updated successfully.",
                    "data": note_serializer,
                }
            ),
            200,
        )

    async def delete_note(self, user, note_id):
        note_data = await NoteDatabase.delete(
            category="delete_note_by_user_id", note_id=note_id, user_id=f"{user.id}"
        )
        return (
            jsonify(
                {
                    "message": "note deleted successfully.",
                    "data": note_data,
                }
            ),
            200,
        )

    async def get_all_notes(self, user):
        note_data = await NoteDatabase.get(
            category="get_all_notes_by_user_id", user_id=f"{user.id}"
        )
        if not note_data:
            return (
                jsonify(
                    {
                        "message": "no notes found",
                        "data": [],
                    }
                ),
                200,
            )
        notes = []
        for note in note_data:
            note_serializer = self.note_serializer.serialize(note)
            notes.append(note_serializer)
        return (
            jsonify(
                {
                    "message": "success get all notes",
                    "data": notes,
                }
            ),
            200,
        )

    async def create_note(self, user, title, note):
        errors = {}
        try:
            note_ai = self.note_ai.summarize_note(note)
        except NoteSummaryParseError:
            errors.setdefault("note", []).append("IS_INVALID")
        if errors:
            return (
                jsonify(
                    {
                        "message": "Failed to create note",
                        "errors": errors,
                    }
                ),
                422,
            )
        note_data = await NoteDatabase.insert(
            user_id=f"{user.id}",
            title=title,
            note=note,
            summary=note_ai["summary"],
            tags=note_ai["bullets"],
        )
        note_serializer = self.note_serializer.serialize(note_data)
        return (
            jsonify(
                {
                    "message": "note created successfully.",
                    "data": note_serializer,
                }
            ),
            201,
        )
