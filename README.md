# 🛒 API de Compras - *Vitto Store*

Esta API foi desenvolvida com **FastAPI** e é responsável por gerenciar os pedidos realizados na loja online *Vitto Store*. O front-end da aplicação consome os dados da **FakeStore API**, enquanto esta API armazena os pedidos dos usuários em um banco de dados local (SQLite).

---

## 📦 Tecnologias Utilizadas

- **FastAPI** (framework web assíncrono)
- **SQLite** (banco de dados leve)
- **Uvicorn** (servidor ASGI)
- **Docker** (containerização da aplicação)
- **FakeStore API** (serviço externo de produtos)

---

## ⚙️ Pré-requisitos

Para executar a aplicação localmente, é necessário ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

---

## ▶️ Executando com Docker

Para executar, basta ir no terminal e ditar o comando:

Constução da Imagem Docker - 
  ```bash
  docker build -t loja-backend .
  ```
Rodar o container - 
```bash
  docker run -p 8000:8000 loja-backend
```
---

## 📊 Diagrama da Arquitetura

[FakeStore API] ---> [ Front-End (HTML/JS) ] ---> [ Vitto Store API (FastAPI) ] ---> [ SQLite DB ]
