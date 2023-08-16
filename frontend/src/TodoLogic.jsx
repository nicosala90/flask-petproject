import { useState } from "react";
import TodoForm from "./TodoForm";
import Todo from "./Todo";

function TodoLogic() {

    const [todos, setTodos] = useState([
        {
            text: "Learn about python",
            isCompleted: false
        },
        {
            text: "Do a Flask project",
            isCompleted: false
        }
    ]);
    const [todoId, setTodoId] = useState("")

    function addTodo(text) {

        fetch('http://localhost:5000/add-data', {
            method: 'POST',
            body: JSON.stringify({
                todo: text,
                isCompleted: false
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(res => res.json())
        .then(id => setTodoId(id))
        
        const newTodos = [...todos, { text }];
        setTodos(newTodos)
    };

    function completeTodo(todoId, index) {

        fetch(`http://localhost:5000/update-todo-status/${todoId}`, {
            method: 'PUT',
            body: JSON.stringify({
                isCompleted: true
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })

        const newTodos = [...todos];
        newTodos[index].isCompleted = true;
        setTodos(newTodos)
    }

    function removeTodo(todoId, index) {
        fetch(`http://localhost:5000/delete/${todoId}`, {
            method: 'DELETE',
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        
        const newTodos = [...todos];
        newTodos.splice(index, 1);
        setTodos(newTodos)
    }


    return (
        <div className="app">
            <div className="todo-list">
                {todos.map((todo, index) => (
                    <Todo
                        key={index}
                        todo={todo}
                        completeTodo={() => completeTodo(index, todo._id)}
                        removeTodo={() => {removeTodo(index, todoId); console.log(todoId)}}
                    />
                ))}
                <TodoForm addTodo={addTodo} />
            </div>
        </div>

    );
}
export default TodoLogic;