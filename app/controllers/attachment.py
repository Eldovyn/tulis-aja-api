from flask import send_file, jsonify, current_app
from ..utils import Validation
import os


class AttachmentController:
    def __init__(self):
        pass

    def get_mascot(self, level):
        errors = {}
        Validation.validate_required_text_sync(errors, "level", level)
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
        if level.lower() == "high":
            level = "1"
        elif level.lower() == "medium":
            level = "2"
        elif level.lower() == "low":
            level = "3"
        else:
            return jsonify({"message": "image not found"}), 404
        fs_path = os.path.join(current_app.static_folder, "img", f"Mascot_{level}.png")
        return send_file(
            fs_path,
            mimetype="image/webp",
            download_name="mascot.webp",
        )
