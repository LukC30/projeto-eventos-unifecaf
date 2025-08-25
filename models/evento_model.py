from dataclasses import dataclass
from typing import Optional, Self

@dataclass
class EventoModel():
    """Essa classe irá representar uma model de um evento no sistema"""
    nome: str
    data: str
    descricao: str
    criador: int
    max_participantes: int
    id: Optional[int] = None    

    @classmethod
    def from_dict(cls, data: dict, creator: str) -> Self:
        """
        Cria uma instancia da própria classe, a partir de uma conversão de Dict
        Popularmente chamado pelas ruas de Mapper
        """

        required_fields = ['nome', 'data', 'descricao', 'max_participantes']
        if not all(key in data for key in required_fields) and creator is '':
            raise ValueError(f"Dados incompletos. Campos obrigatórios: {required_fields}")
        return cls(
            nome = data['nome'],
            data = data['data'],
            descricao = data['descricao'],
            max_participantes = data['max_participantes']
        )