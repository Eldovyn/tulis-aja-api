import mongoengine as me
from .base import BaseDocument
from .users import UsersModel


class RolePlayChatModel(BaseDocument):
    room = me.StringField(required=True)
    original_message = me.StringField(required=True)
    response_message = me.StringField(required=True)

    user = me.ReferenceField(UsersModel, required=True, reverse_delete_rule=me.CASCADE)
    meta = {"collection": "roleplay_chat"}
