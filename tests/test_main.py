# testes da api
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_criar_tarefa():

    response = client.post(
        "/tarefas",
        json={
            "id": 1,
            "titulo": "Estudar FastAPI",
            "concluida": False
        }
    )

    assert response.status_code == 200


def test_listar_tarefas():

    response = client.get("/tarefas")

    assert response.status_code == 200


def test_buscar_tarefa():

    response = client.get("/tarefas/1")

    assert response.status_code == 200


def test_atualizar_tarefa():

    response = client.put(
        "/tarefas/1",
        json={
            "id": 1,
            "titulo": "FastAPI atualizado",
            "concluida": True
        }
    )

    assert response.status_code == 200


def test_deletar_tarefa():

    response = client.delete("/tarefas/1")

    assert response.status_code == 200