import mongoengine as me
from .base import BaseDocument
from .users import UsersModel


class BlacklistTokenModel(BaseDocument):
    created_at = me.IntField(required=True)

    user = me.ReferenceField(UsersModel, reverse_delete_rule=me.CASCADE)

    meta = {"collection": "blacklist_token"}
