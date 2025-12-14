from ..serializers import RoadmapSerializer
from ..utils import Validation
from flask import jsonify
from ..dataclasses import RoadmapSchema


class RoadmapControllers:
    def __init__(self):
        self.roadmap_serializer = RoadmapSerializer()

    def roadmap_compact(self, roadmap_name):
        errors = {}
        Validation.validate_required_text_sync(errors, "roadmap_name", roadmap_name)
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
        data_roadmap = []
        if roadmap_name.lower() == "product & ux":
            _data_roadmap_1 = RoadmapSchema(
                title="Product Manager",
                description="Peta jalan ini memandu belajar menjadi Product Manager, dari memahami kebutuhan pengguna hingga memimpin strategi produk",
            )
            data_roadmap.append(_data_roadmap_1)
            _data_roadmap_2 = RoadmapSchema(
                title="Product Designer",
                description="Peta jalan ini memandu belajar menjadi Product Designer, dari konsep produk hingga menyatukan UX, UI, dan strategi bisnis.",
            )
            data_roadmap.append(_data_roadmap_2)
        elif roadmap_name.lower() == "mobile development":
            _data_roadmap_1 = RoadmapSchema(
                title="Mobile App Developer",
                description="Peta jalan ini menjelaskan tahapan belajar menjadi Mobile App Developer, dari dasar hingga mahir membuat aplikasi mobile profesional.",
            )
            data_roadmap.append(_data_roadmap_1)
            _data_roadmap_2 = RoadmapSchema(
                title="Mobile Back-End",
                description="Peta jalan ini menjelaskan tahapan belajar menjadi Mobile Back-End Developer, dari dasar hingga mahir mengelola sistem untuk aplikasi mobile.",
            )
            data_roadmap.append(_data_roadmap_2)
        elif roadmap_name.lower() == "data & ai":
            _data_roadmap_1 = RoadmapSchema(
                title="Data Scientist",
                description="Peta jalan ini memandu belajar menjadi Data Scientist, dari analisis data dasar hingga membangun model prediktif kompleks.",
            )
            data_roadmap.append(_data_roadmap_1)
            _data_roadmap_2 = RoadmapSchema(
                title="Machine Learning Engineer",
                description="Peta jalan ini memandu belajar menjadi Machine Learning Engineer, dari algoritma dasar hingga mengembangkan dan menerapkan model AI/ML.",
            )
            data_roadmap.append(_data_roadmap_2)
        elif roadmap_name.lower() == "web development":
            _data_roadmap_1 = RoadmapSchema(
                title="Front-End Developer",
                description="Peta jalan ini menjelaskan tahapan belajar menjadi Front-End Developer, dari dasar hingga mahir membangun antarmuka pengguna yang interaktif.",
            )
            data_roadmap.append(_data_roadmap_1)
            _data_roadmap_2 = RoadmapSchema(
                title="Back-End Developer",
                description="Peta jalan ini menjelaskan tahapan belajar menjadi Back-End Developer, dari dasar hingga mahir membangun dan mengelola sistem di sisi server.",
            )
            data_roadmap.append(_data_roadmap_2)
        else:
            return jsonify({"message": "roadmap not found"}), 404
        data_roadmap_serialized = [
            self.roadmap_serializer.serialize(roadmap) for roadmap in data_roadmap
        ]
        return (
            jsonify(
                {
                    "message": "roadmap retrieved successfully",
                    "data": data_roadmap_serialized,
                }
            ),
            200,
        )
