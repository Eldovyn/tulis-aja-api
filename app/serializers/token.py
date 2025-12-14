from ..dataclasses import AccessTokenSchema
from .interfaces import SerializerInterface
from typing import Union
from dataclasses import asdict


class TokenSerializer(SerializerInterface):
    def serialize(
        self,
        token_data: Union[AccessTokenSchema],
        access_token_is_null: bool = False,
        token_is_null: bool = False,
        created_at_is_null: bool = False,
    ) -> dict:
        out = asdict(token_data)
        if created_at_is_null:
            out.pop("created_at", None)
        if isinstance(token_data, AccessTokenSchema):
            if access_token_is_null:
                out.pop("access_token", None)
        return out
