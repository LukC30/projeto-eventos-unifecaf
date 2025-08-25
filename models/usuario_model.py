from dataclasses import dataclass
from typing import Optional, Self

@dataclass
class UsuarioModel():
    """Representa um usuário (aluno ou coordenador) no sistema."""
    nome:str
    email: str
    tipo: str
    id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """
        Cria uma instancia da própria classe, a partir de uma conversão de Dict
        Popularmente chamado pelas ruas de Mapper
        """

        required_fields = ['nome', 'email', 'tipo']
        if not all(key in data for key in required_fields):
            raise ValueError(f"Faltando campos obrigatórios: {required_fields}")
        
        return cls(
            nome=data['nome'],
            email=data['email'],
            tipo=data['tipo']
        )