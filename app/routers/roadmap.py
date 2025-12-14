from flask import Blueprint
from ..controllers import RoadmapControllers

roadmap_router = Blueprint("roadmap_router", __name__)
roadmap_controllers = RoadmapControllers()


@roadmap_router.get("/<string:roadmap_name>/compact")
def roadmap_compact(roadmap_name):
    return roadmap_controllers.roadmap_compact(roadmap_name)
