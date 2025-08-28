import sqlite3
import logging
from ..repository.evento_repository import EventoRepository
from ..models.evento_model import EventoModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class EventoService():
    """
    Classe de serviço, responsavel por regras de serviço 
    """
    def __init__(self, repo: EventoRepository):
        self._repo = repo

    def create_event(self, event_data: dict, creator_login: str):
 
        event_model = EventoModel(**event_data)

        try:
            new_event = self._repo.create_event(event_model, creator_login)
            logging.info(f"Evento '{new_event.nome}' criado com sucesso.")
            return new_event
        except sqlite3.Error as e:
            logging.error(f"Erro no banco de dados ao criar um evento: {e}")
            raise ValueError(f"Erro interno {e}")
    
    
    def get_events(self):
        try:
            all_events = self._repo.get_events()
            logging.info(f"Todos os eventos foram recuperados")
            return all_events    
                
        except sqlite3.Error as e:
            logging.error(f"Erro no banco de dados ao buscar os eventos: {e}")
            raise ValueError(f"Erro interno {e}")


    def update_event(self, event_data: dict):

        event_model = EventoModel(**event_data)

        try:
            updated_event = self._repo.update_event(event_model)
            logging.info(f"Evento '{updated_event} foi alterado com sucesso.'")
            return updated_event
        except sqlite3.Error as e:
            logging.error(f"Erro no banco de dados ao atualizar o evento: {e}")
            raise ValueError(f"Erro interno {e}")


    def delete_event(self, event_id: int):

        try:
            deleted_event = self._repo.delete_event(event_id)
            logging.info(f"Evento de id: '{event_id}' foi deletado")
            return deleted_event
        
        except sqlite3.Error as e:
            logging.error(f"Erro no banco de dados ao deletar o evento: {e}")
            raise ValueError(f"Erro interno {e}")