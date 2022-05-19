from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk
import logging


api_blueprint = Blueprint("api_blueprint", __name__)

logging.basicConfig(level=logging.INFO)

logger_api = logging.getLogger("api")
file_handler_api = logging.FileHandler("logs/api.log")
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler_api.setFormatter(formatter_api)
logger_api.addHandler(file_handler_api)


@api_blueprint.route("/posts/")
def get_posts():
    logger_api.info("Запрос /api/posts")
    return jsonify(get_posts_all())


@api_blueprint.route("/posts/<int:pk>")
def get_post(pk):
    logger_api.info(f"Запрос /api/posts/{pk}")
    return jsonify(get_post_by_pk(pk))
