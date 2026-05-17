from fastapi import FastAPI, HTTPException
from app.models import Tarefa
from app.database import tarefas

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando!"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa.dict())

    return {
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": tarefa
    }


@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, nova_tarefa: Tarefa):

    for index, tarefa in enumerate(tarefas):

        if tarefa["id"] == tarefa_id:
            tarefas[index] = nova_tarefa.dict()

            return {
                "mensagem": "Tarefa atualizada"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):

    for index, tarefa in enumerate(tarefas):

        if tarefa["id"] == tarefa_id:
            tarefas.pop(index)

            return {
                "mensagem": "Tarefa removida"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )