from ..serializers import UserSerializer
from flask import jsonify


class UserController:
    def __init__(self):
        self.user_seliazer = UserSerializer()

    async def user_me(self, user):
        user_serializer = self.user_seliazer.serialize(user)
        return (
            jsonify(
                {
                    "message": "success get user",
                    "data": user_serializer,
                }
            ),
            200,
        )
