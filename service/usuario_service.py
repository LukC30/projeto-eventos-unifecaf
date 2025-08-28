import sqlite3
import logging
from ..repository.usuario_repository import UsuarioRepository
from ..models.usuario_model import UsuarioModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UsuarioService():
    def __init__(self, repo: UsuarioRepository):
        self._repo = repo
    
    def create_user(self, user_data: dict):

        user_model = UsuarioModel(**user_data)
        try:
            user_created = self._repo.create_user(user_model)
            logging.info(f"Usuario '{user_created.nome}' criado com o id '{user_created.id}'")
            return user_created
        
        except sqlite3.Error as e:
            logging.error(f'Erro ao criar o usuario: {e}')
            raise ValueError(f'Erro interno do servidor: {e}')