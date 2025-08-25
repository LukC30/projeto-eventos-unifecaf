import sqlite3
from typing import List
from ..models.inscricao_model import InscricaoModel

class InscricaoRepository():

    def __init__(self, db_path):
        self._db_path = db_path

    
    def create_event(self, subscribe: InscricaoModel):

        conn = sqlite3.connect(self._db_path)
        if not conn:
            return False
        
        cursor = conn.cursor()

        sql = """INSERT INTO tbl_inscricoes(id_evento, id_usuario)"""
        try:
            cursor.execute(sql, (
                subscribe.id_evento,
                subscribe.id_usuario
            ))
            conn.commit()

        finally:
            if conn:
                conn.close()


    def get_by_event(self, event_id) -> List[InscricaoModel]:

        conn = sqlite3.connect(self._db_path)
        if not conn:
            return False
                
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = """SELECT * FROM tbl_inscricoes WHERE id_evento = ?"""
        try:
            cursor.execute(sql, (event_id, ))
            rows = cursor.fetchall()
            if rows > 0:
                return [InscricaoModel(**row) for row in rows]
        finally:
            if conn:
                conn.close()