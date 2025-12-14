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
        pass

    @staticmethod
    async def update(category, **kwargs):
        pass

    @staticmethod
    async def get(category, **kwargs):
        user_id = kwargs.get("user_id")
        if category == "get_all_notes_by_user_id":
            if user_data := UsersModel.objects(id=user_id).first():
                if note_data := NoteModel.objects(user=user_data).all():
                    return note_data
