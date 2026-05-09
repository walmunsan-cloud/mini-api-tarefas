from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mini API de Tarefas")


class Task(BaseModel):
    id: int
    titulo: str
    concluida: bool = False


tasks = []


@app.get("/")
def home():
    return {"mensagem": "API funcionando com sucesso"}


@app.get("/tarefas")
def listar_tarefas():
    return tasks


@app.post("/tarefas")
def criar_tarefa(task: Task):
    tasks.append(task.dict())
    return task