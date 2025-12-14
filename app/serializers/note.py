from ..models import NoteModel
from .interfaces import SerializerInterface


class NoteSerializer(SerializerInterface):
    def serialize(
        self,
        note: NoteModel,
        id_is_null: bool = False,
        title_is_null: bool = False,
        content_is_null: bool = False,
        summary_is_null: bool = False,
        tags_is_null: bool = False,
        created_at_is_null: bool = False,
        updated_at_is_null: bool = False,
        deleted_at_is_null: bool = False,
    ) -> dict:
        data = {}
        if not id_is_null and note.id:
            data["id"] = str(note.id) if note.id else None
        if not title_is_null and note.title:
            data["title"] = note.title
        if not content_is_null and note.content:
            data["content"] = note.content
        if not summary_is_null and note.summary:
            data["summary"] = note.summary
        if not created_at_is_null and note.created_at:
            data["created_at"] = note.created_at.isoformat()
        if not updated_at_is_null and note.updated_at:
            data["updated_at"] = note.updated_at.isoformat()
        if not deleted_at_is_null and note.deleted_at:
            data["deleted_at"] = note.deleted_at.isoformat()
        if not tags_is_null and note.tags:
            data["tags"] = note.tags
        return data
