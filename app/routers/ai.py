from flask import Blueprint, request
from ..utils import jwt_required
from ..controllers import AIController

ai_router = Blueprint("ai_router", __name__)
ai_controller = AIController()


@ai_router.post("/assesment")
@jwt_required()
async def ai_assesment():
    data = request.json
    user = request.user
    timestamp = request.timestamp
    q1 = data.get("Q1", "")
    q2 = data.get("Q2", "")
    q3 = data.get("Q3", "")
    q4 = data.get("Q4", "")
    q5 = data.get("Q5", "")
    q6 = data.get("Q6", "")
    q7 = data.get("Q7", "")
    q8 = data.get("Q8", "")
    q9 = data.get("Q9", "")
    q10 = data.get("Q10", "")
    q11 = data.get("Q11", "")
    q12 = data.get("Q12", "")
    q13 = data.get("Q13", "")
    q14 = data.get("Q14", "")
    q15 = data.get("Q15", "")
    return await ai_controller.ai_assesment(
        user,
        {
            "Q1": q1,
            "Q2": q2,
            "Q3": q3,
            "Q4": q4,
            "Q5": q5,
            "Q6": q6,
            "Q7": q7,
            "Q8": q8,
            "Q9": q9,
            "Q10": q10,
            "Q11": q11,
            "Q12": q12,
            "Q13": q13,
            "Q14": q14,
            "Q15": q15,
        },
    )
