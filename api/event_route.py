import sqlite3
from dataclasses import asdict
from flask import Blueprint, jsonify, request
from ..service.evento_service import EventoService
from ..repository.evento_repository import EventoRepository
from ..db.setup import DB_PATH

event_api = Blueprint('event_routes', __name__)

event_repository = EventoRepository(DB_PATH)
event_service = EventoService(event_repository)

@event_api.route('/event/create', methods=['POST'])
def create_event():
    event_data = request.get_json()

    if not event_data:
        return jsonify({"message" : "O corpo da requisição não pode ser vazio"})
    
    try:
        new_event = event_service.create_event(event_data)

        return jsonify(asdict(new_event)), 201

    except (ValueError, sqlite3.Error) as e:
        return jsonify({"error" : f"{str(e)}"}), 401