from pydantic import BaseModel

class Task(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False