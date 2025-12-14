from flask import Blueprint, request
from ..controllers import RegisterController, LoginController

auth_router = Blueprint("auth_router", __name__)
register_controller = RegisterController()
login_controller = LoginController()


@auth_router.post("/register")
async def user_register():
    data = request.json
    username = data.get("username", "")
    email = data.get("email", "")
    password = data.get("password", "")
    confirm_password = data.get("confirm_password", "")
    provider = data.get("provider", "")
    return await register_controller.user_register(
        provider,
        username,
        email,
        password,
        confirm_password,
    )


@auth_router.post("/login")
async def user_login():
    data = request.json
    timestamp = request.timestamp
    email = data.get("email", "")
    password = data.get("password", "")
    provider = data.get("provider", "")
    return await login_controller.user_login(provider, email, password, timestamp)
