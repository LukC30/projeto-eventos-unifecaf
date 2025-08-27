import sqlite3
from flask import Blueprint, jsonify, request
from dataclasses import asdict
from ..service.usuario_service import UsuarioService
from ..repository.usuario_repository import UsuarioRepository

from ..db.setup import DB_PATH

user_api = Blueprint('user_api', __name__)

user_repo = UsuarioRepository(DB_PATH)
user_service = UsuarioService(user_repo)

@user_api.route('/user/create', methods=['POST'])
def post_user():
    user_data = request.get_json()

    if not user_data or not all(key in user_data for key in ['nome', 'email', 'tipo']):
        return jsonify({"message" : "Erro na falta dos dados"}), 400
    
    try:
        new_user = user_service.create_user(user_data)

        return jsonify(asdict(new_user)), 201
    
    except (ValueError, sqlite3.Error) as e:
        return jsonify({"Error" : str(e)}), 400