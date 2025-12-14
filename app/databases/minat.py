from .database import Database
from ..models import UsersModel, MinatModel


class MinatDatabase(Database):
    @staticmethod
    async def insert(user_id, minat):
        if user_data := UsersModel.objects(id=user_id).first():
            if minat_data := MinatModel.objects(user=user_data).first():
                minat_data.minat = minat
                minat_data.save()
            else:
                minat_data = MinatModel(user=user_data, minat=minat)
                minat_data.save()
            return minat_data

    @staticmethod
    async def delete(category, **kwargs):
        pass

    @staticmethod
    async def update(category, **kwargs):
        pass

    @staticmethod
    async def get(category, **kwargs):
        user_id = kwargs.get("user_id")
        if category == "get_minat_by_user_id":
            if user_data := UsersModel.objects(id=user_id).first():
                if minat_data := MinatModel.objects(user=user_data).first():
                    return minat_data
