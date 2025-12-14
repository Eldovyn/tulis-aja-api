import mongoengine as me
from .base import BaseDocument
from .users import UsersModel


class AccountActiveModel(BaseDocument):
    token = me.StringField(required=True)
    otp = me.StringField(required=True)
    expired_at = me.DateTimeField(required=True)

    user = me.ReferenceField(
        UsersModel, required=True, unique=True, reverse_delete_rule=me.CASCADE
    )

    meta = {"collection": "account_active"}
