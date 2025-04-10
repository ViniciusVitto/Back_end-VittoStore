from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import sqlite3

app = FastAPI()

FAKESTORE_URL = "https://fakestoreapi.com/products"

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique: ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelo de Pedido
class Pedido(BaseModel):
    produto_id: int
    quantidade: int
    cliente: str

# Banco de Dados SQLite (simples)
conn = sqlite3.connect("banco.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    cliente TEXT
)
""")
conn.commit()

# Rota para listar produtos da FakeStore API
@app.get("/produtos")
def listar_produtos():
    response = requests.get(FAKESTORE_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao buscar produtos")
    return response.json()

# Rota para criar um novo pedido
@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    cursor.execute("INSERT INTO pedidos (produto_id, quantidade, cliente) VALUES (?, ?, ?)",
                   (pedido.produto_id, pedido.quantidade, pedido.cliente))
    conn.commit()
    return {"mensagem": "Pedido criado com sucesso!"}

# Rota para listar todos os pedidos
@app.get("/pedidos")
def listar_pedidos():
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    return [{"id": p[0], "produto_id": p[1], "quantidade": p[2], "cliente": p[3]} for p in pedidos]

# Rota para deletar um pedido
@app.delete("/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int):
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    conn.commit()
    return {"mensagem": "Pedido deletado com sucesso!"}

# Rota para atualizar um pedido
@app.put("/pedidos/{pedido_id}")
def atualizar_pedido(pedido_id: int, pedido: Pedido):
    cursor.execute("UPDATE pedidos SET produto_id = ?, quantidade = ?, cliente = ? WHERE id = ?",
                   (pedido.produto_id, pedido.quantidade, pedido.cliente, pedido_id))
    conn.commit()
    return {"mensagem": "Pedido atualizado com sucesso!"}
