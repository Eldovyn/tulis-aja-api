from .database import Database
from ..models import UsersModel, NoteModel


class NoteDatabase(Database):
    @staticmethod
    async def insert(user_id, title, note, summary, tags):
        if user_data := UsersModel.objects(id=user_id).first():
            if note_data := NoteModel.objects(user=user_data).first():
                note_data.title = title
                note_data.content = note
                note_data.summary = summary
                note_data.tags = tags
                note_data.save()
            else:
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
        pass
