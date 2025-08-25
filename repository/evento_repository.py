import sqlite3
from typing import List
from ..models.evento_model import EventoModel

class EventoRepository():

    def __init__(self, db_path: str):
        """
        Vamos inicializar o banco por aqui
        """
        self._db_path = db_path



    def create_event(self, event: EventoModel, login: str) -> EventoModel:
        
        conn = sqlite3.connect(self._db_path)
        if not conn:
            return print("Conexão não deu certo")
        cursor = conn.cursor()

        sql = """
            INSERT INTO tbl_eventos(nome, data, descricao, max_participantes, criador) VALUES(?,?,?,?,?)
        """

        cursor.execute(
            sql, (
            event.nome,
            event.data,
            event.descricao,
            event.max_participantes,
            login
            ))
        
        new_id = cursor.lastrowid

        conn.commit()
        conn.close()

        event.id = new_id
        return event
    
    def get_event_by_id(self, event_id: int) -> EventoModel:
        conn = sqlite3.connect(self._db_path)
        if not conn:
            return print("Conexão não deu certo")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = """
            SELECT * FROM tbl_eventos WHERE id = ?        
        """

        cursor.execute(sql, (event_id, ))
        row = cursor.fetchone()
        if row:
            conn.close()
            return EventoModel(**row)
        conn.close()
        return print(f"Erro na extração de dados")


    def get_events(self) -> List[EventoModel]:
        
        conn = sqlite3.connect(self._db_path)
        if not conn:
            return 
  
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = """SELECT * FROM tbl_evento"""
        
        try:
            cursor.execute(sql)
            events = cursor.fetchall()
            return[EventoModel(**row) for row in events]
        finally:
            if conn:
                conn.close()

    def update_event(self, event: EventoModel):
        data = self.get_event_by_id(event.id)
        if not data:
            return print("O evento buscado nao existe")
        
        conn = sqlite3.connect(self._db_path)
        if not conn:
            return print("Brutal nao sobra nada para a conexão")
        
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = """update from tbl_evento set data = ?, descricao = ?, criador = ? where id = ?"""
        try:
            cursor.execute(sql, (
                event.data,
                event.descricao,
                event.criador,
                event.id
            ))
            conn.commit()
        finally:
            if conn:
                conn.close()

    def delete_event(self, event_id):

        conn = None
        try:
            data = self.get_event_by_id(event_id)
            if not data:
                return False
            
            conn = sqlite3.connect(self._db_path)
            if not conn:
                return False

            cursor = conn.cursor()

            sql = '''DELETE FROM tbl_evento WHERE id = ?'''

            cursor.execute(sql, (event_id, ))
            conn.commit()
            if cursor.rowcount > 0:
                return data
            return False
        
        finally:
            if conn:
                conn.close()
