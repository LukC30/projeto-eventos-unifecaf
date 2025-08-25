from dataclasses import dataclass
from typing import Optional

@dataclass
class InscricaoModel():
    """Representa a inscrição de um usuário em um evento."""
    id_usuario: int
    id_evento: int
    id: Optional[int] = None
