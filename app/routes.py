from datetime import datetime

from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=['GET'])
def get_info():
    """Returns basic information in JSON format."""

    response = {
        "email": "abdurrahmaneedrees@gmail.com",
        "current_datetime": datetime.now().isoformat() + "Z",
        "github_url": "https://github.com/AbdurrahmanIdr/hng12-api.git"
    }

    return jsonify(response), 200
