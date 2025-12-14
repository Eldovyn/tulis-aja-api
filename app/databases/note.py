from .database import Database
from ..models import UsersModel, NoteModel


class NoteDatabase(Database):
    @staticmethod
    async def insert(user_id, title, note, summary, tags):
        if user_data := UsersModel.objects(id=user_id).first():
            note_data = NoteModel(
                user=user_data,
                title=title,
                content=note,
                summary=summary,
                tags=tags,
            )
            note_data.save()
            return note_data

    @staticmethod
    async def delete(category, **kwargs):
        user_id = kwargs.get("user_id")
        if category == "delete_note_by_user_id":
            if user_data := UsersModel.objects(id=user_id).first():
                if note_data := NoteModel.objects(user=user_data).first():
                    note_data.delete()
                    return note_data

    @staticmethod
    async def update(category, **kwargs):
        user_id = kwargs.get("user_id")
        title = kwargs.get("title")
        content = kwargs.get("content")
        note_id = kwargs.get("note_id")
        summary = kwargs.get("summary")
        tags = kwargs.get("tags")
        if category == "update_note_by_user_id":
            if user_data := UsersModel.objects(id=user_id).first():
                if note_data := NoteModel.objects(id=note_id).first():
                    note_data.title = title
                    note_data.content = content
                    note_data.summary = summary
                    note_data.tags = tags
                    note_data.save()
                    return note_data

    @staticmethod
    async def get(category, **kwargs):
        user_id = kwargs.get("user_id")
        if category == "get_all_notes_by_user_id":
            if user_data := UsersModel.objects(id=user_id).first():
                if note_data := NoteModel.objects(user=user_data).all():
                    return note_data
