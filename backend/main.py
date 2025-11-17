from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

# 削除用API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    # todos の中から id が一致するものを探して削除
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return {"message": "deleted"}

    # 見つからなかった場合は 404 エラー
    raise HTTPException(status_code=404, detail="Todo not found")