import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');

  // FastAPI から TODO リストを取得
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/todos')
      .then(res => setTodos(res.data))
      .catch(err => console.error(err));
  }, []);

  // TODO を追加
  const addTodo = (e) => {
    e.preventDefault();
    const newTodo = {
      id: todos.length + 1,
      title: title,
      done: false
    };

    axios.post('http://127.0.0.1:8000/todos', newTodo)
      .then((res) => {
        setTodos([...todos, res.data]);
        setTitle('');
      })
      .catch(err => console.error(err));
  };

  // TODO を削除
  const deleteTodo = (id) => {
    axios.delete(`http://127.0.0.1:8000/todos/${id}`)
      .then(() => {
        // 削除した TODO を除いた配列に更新
        setTodos(todos.filter((todo) => todo.id !== id));
      })
      .catch((err) => {
        console.error(err);
        alert("削除に失敗しました");
      });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>TODO リスト</h1>

      <form onSubmit={addTodo}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="新しい TODO"
          required
        />
        <button type="submit">追加</button>
      </form>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.title}
            <button
              style={{ marginLeft: "8px" }}
              onClick={() => deleteTodo(todo.id)}
            >
              削除
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;