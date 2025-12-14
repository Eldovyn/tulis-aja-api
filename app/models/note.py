import mongoengine as me
from .base import BaseDocument
from .users import UsersModel


class NoteModel(BaseDocument):
    title = me.StringField(required=True)
    content = me.StringField(required=True)
    summary = me.StringField(required=True)
    tags = me.ListField(required=True)

    user = me.ReferenceField(
        UsersModel, required=True, unique=True, reverse_delete_rule=me.CASCADE
    )

    meta = {"collection": "note"}
