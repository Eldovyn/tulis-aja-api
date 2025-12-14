from ..databases import (
    UserDatabase,
)
from flask import jsonify
from ..utils import (
    AuthJwt,
    Validation,
)
from ..serializers import UserSerializer, TokenSerializer
from ..dataclasses import AccessTokenSchema


class LoginController:
    def __init__(self):
        self.user_seliazer = UserSerializer()
        self.token_serializer = TokenSerializer()

    async def user_login(self, provider, email, password, timestamp):
        from ..extensions import bcrypt

        access_token = None
        errors = {}
        await Validation.validate_provider_async(errors, provider)
        await Validation.validate_required_text_async(errors, "email", email)
        await Validation.validate_required_text_async(errors, "password", password)
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
        if not (user_data := await UserDatabase.get("get_user_by_email", email=email)):
            return (
                jsonify(
                    {
                        "message": "invalid email or password",
                    }
                ),
                401,
            )
        if not bcrypt.check_password_hash(user_data.password, password):
            return (
                jsonify(
                    {
                        "message": "invalid email or password",
                    }
                ),
                401,
            )
        access_token = await AuthJwt.generate_jwt_async(f"{user_data.id}", timestamp)
        user_me = self.user_seliazer.serialize(user_data)
        token_model = AccessTokenSchema(access_token, timestamp)
        token_data = self.token_serializer.serialize(token_model)
        return (
            jsonify(
                {
                    "message": "user login successfully",
                    "data": user_me,
                    "token": token_data,
                }
            ),
            201,
        )
