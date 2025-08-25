import sqlite3
from typing import List

from ..models.usuario_model import UsuarioModel

class UsuarioRepository():
    def __init__(self, db_path: str):
        
        self._db_path = db_path


    def create_user(self, usuario: UsuarioModel):
        
        conn = sqlite3.connect(self._db_path)
        if not conn:
            return False
        cursor = conn.cursor()

        sql = """INSERT INTO tbl_usuarios(nome, email, tipo) VALUES (?,?,?)"""

        try:
            cursor.execute(sql, (
                usuario.nome,
                usuario.email,
                usuario.tipo
            ))
            conn.commit()
            return usuario
        finally:
            if conn:
                conn.close()