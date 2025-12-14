from .database import Database
from ..models import UsersModel


class UserDatabase(Database):
    @staticmethod
    async def insert(
        provider,
        avatar,
        username,
        email,
        password,
    ):
        user_data = UsersModel(
            email=email,
            username=username,
            password=password,
            provider=provider,
            avatar=avatar,
        )
        user_data.is_active = True
        await user_data.unique_field()
        user_data.save()
        return user_data

    @staticmethod
    async def delete(category, **kwargs):
        pass

    @staticmethod
    async def update(category, **kwargs):
        pass

    @staticmethod
    async def get(category, **kwargs):
        email = kwargs.get("email")
        user_id = kwargs.get("user_id")
        if category == "get_user_by_email":
            if user_data := UsersModel.objects(email=email.lower()).first():
                return user_data
        if category == "get_user_by_id":
            if user_data := UsersModel.objects(id=user_id).first():
                return user_data
