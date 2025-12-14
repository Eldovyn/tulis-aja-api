import mongoengine as me
from .users import UsersModel
from .base import BaseDocument


class MinatModel(BaseDocument):
    minat = me.ListField(required=True)

    user = me.ReferenceField(
        UsersModel, required=True, unique=True, reverse_delete_rule=me.CASCADE
    )

    meta = {"collection": "minat"}
