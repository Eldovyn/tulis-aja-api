from .database import Database
from ..models import RolePlayChatModel, UsersModel


class RolePlayDatabase(Database):
    @staticmethod
    async def insert(user_id, original_message, response_message):
        pass

    @staticmethod
    def insert_sync(user_id, room, original_message, response_message):
        if user_data := UsersModel.objects(id=user_id).first():
            role_play = RolePlayChatModel(
                room=room,
                original_message=original_message,
                response_message=response_message,
                user=user_data,
            )
            role_play.save()
            return role_play

    @staticmethod
    async def delete(category, **kwargs):
        pass

    @staticmethod
    async def update(category, **kwargs):
        pass

    @staticmethod
    async def get(category, **kwargs):
        pass
