from flask import Blueprint, request
from ..utils import jwt_required
from ..controllers import UserController

user_router = Blueprint("user_router", __name__)
user_controller = UserController()


@user_router.get("/@me")
@jwt_required()
async def user_me():
    user = request.user
    return await user_controller.user_me(user)
