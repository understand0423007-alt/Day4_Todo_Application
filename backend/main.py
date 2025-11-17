from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定（あとで React から叩けるように）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React開発用
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO1件分の型定義
class Todo(BaseModel):
    id: int
    title: str
    done: bool = False

# 仮のデータベース（メモリ上）
todos: list[Todo] = []

# 一覧取得
@app.get("/todos")
def get_todos():
    return todos

# 新規追加
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo