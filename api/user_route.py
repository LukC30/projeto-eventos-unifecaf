from flask import Blueprint, jsonify, routes
from dataclasses import asdict
from ..service.usuario_service import UsuarioService
from ..repository.usuario_repository import UsuarioRepository

from ..db.setup import DB_PATH

user_api = Blueprint('event_api', routes)

user_repo = UsuarioRepository(DB_PATH)
user_service = UsuarioService(user_repo)

@user_api.route('/user/create', methods=['POST'])
def create_user():
    return