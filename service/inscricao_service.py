import sqlite3
import logging
from ..repository.inscricao_repository import InscricaoRepository
from ..models.inscricao_model import InscricaoModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InscricaoService():
    def __init__(self, repo: InscricaoRepository):
        self._repo = repo

    def create_event(self, event_data, user_data):
        """
        Cria uma nova inscrição de um usuário em um evento.
        Verifica se a inscrição já existe antes de criar.
        """
        try:
            id_evento = event_data.get('id_evento')
            id_usuario = user_data.get('id_usuario')

            if not id_evento or not id_usuario:
                logging.warning("Tentativa de inscrição sem ID do evento ou do usuário.")
                return {"message": "ID do evento e do usuário são obrigatórios."}, 400

            nova_inscricao = InscricaoModel(id_usuario=id_usuario, id_evento=id_evento)
            inscricao_criada = self._repo.create(nova_inscricao)
            logging.info(f"Inscrição criada com sucesso: Usuário {id_usuario}, Evento {id_evento}")
            return inscricao_criada.to_dict(), 201

        except sqlite3.Error as e:
            logging.error(f"Erro de banco de dados ao criar inscrição: {e}")
            return {"message": "Erro interno do servidor ao criar inscrição."}, 500
        except Exception as e:
            logging.error(f"Erro inesperado ao criar inscrição: {e}")
            return {"message": "Ocorreu um erro inesperado."}, 500