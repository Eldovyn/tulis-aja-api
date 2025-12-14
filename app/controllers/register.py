from ..databases import UserDatabase
from flask import jsonify, url_for
from ..utils import (
    Validation,
)
from ..serializers import UserSerializer


class RegisterController:
    def __init__(self):
        self.user_seliazer = UserSerializer()

    async def user_register(
        self,
        provider,
        username,
        email,
        password,
        confirm_password,
    ):
        from ..extensions import bcrypt

        errors = {}
        await Validation.validate_provider_async(errors, provider)
        await Validation.validate_username_async(errors, username)
        await Validation.validate_email_async(errors, email)
        await Validation.validate_password_async(errors, password, confirm_password)
        if errors:
            return (
                jsonify(
                    {
                        "errors": errors,
                        "message": "validations error",
                    }
                ),
                400,
            )
        result_password = bcrypt.generate_password_hash(password).decode("utf-8")
        avatar = url_for(
            "static", filename="images/default-avatar.webp", _external=True
        )
        if user_data := await UserDatabase.get("by_email", email=email):
            return (
                jsonify(
                    {
                        "message": "the user already exists",
                    }
                ),
                409,
            )
        if provider != "google":
            user_data = await UserDatabase.insert(
                provider,
                f"{avatar}",
                username,
                email,
                result_password,
            )
            user_me = self.user_seliazer.serialize(user_data)
        return (
            jsonify(
                {
                    "message": "user registered successfully",
                    "data": user_me,
                }
            ),
            201,
        )
