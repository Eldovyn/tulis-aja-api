from ..utils import AiAssesment
from flask import jsonify, url_for
from ..databases import MinatDatabase
from ..serializers import TokenSerializer


class AIController:
    def __init__(self):
        from .. import BASE_DIR

        self.__ai_assesment = AiAssesment(f"{BASE_DIR}/model_nusaCode.pkl")
        self.token_serializer = TokenSerializer()

    async def ai_assesment(self, user, answers):
        hasil = self.__ai_assesment.predict(answers)
        for index, item in enumerate(hasil):
            if index == 0:
                hasil[index]["image"] = url_for(
                    "attachment_router.get_mascot", level="high", _external=True
                )
            elif index == 1:
                hasil[index]["image"] = url_for(
                    "attachment_router.get_mascot", level="medium", _external=True
                )
            else:
                hasil[index]["image"] = url_for(
                    "attachment_router.get_mascot", level="low", _external=True
                )
        await MinatDatabase.insert(f"{user.id}", hasil)
        return (
            jsonify(
                {
                    "message": "success get ai assesment",
                    "data": hasil,
                }
            ),
            201,
        )
