from ..databases import MinatDatabase
from ..serializers import UserSerializer
from flask import jsonify


class UserController:
    def __init__(self):
        self.user_seliazer = UserSerializer()

    async def user_me(self, user):
        if not (
            minat_data := await MinatDatabase.get(
                "get_minat_by_user_id", user_id=f"{user.id}"
            )
        ):
            return jsonify({"message": "minat not found"}), 404
        user_serializer = self.user_seliazer.serialize(minat_data.user)
        return (
            jsonify(
                {
                    "message": "success get user",
                    "data": user_serializer,
                    "minat": minat_data.minat,
                }
            ),
            200,
        )
