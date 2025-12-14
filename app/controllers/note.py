from ..databases import NoteDatabase
from ..serializers import NoteSerializer
from flask import jsonify
from ..utils import NoteAI


class NoteController:
    def __init__(self):
        self.note_serializer = NoteSerializer()
        self.note_ai = NoteAI()

    async def create_note(self, user, title, note):
        note_ai = self.note_ai.summarize_note(note)
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
