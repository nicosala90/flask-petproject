import { useState } from "react";
import TodoForm from "./TodoForm";
import Todo from "./Todo";
function TodoLogic() {


    const [todos, setTodos] = useState([
        {
            text: "Learn about React",
            isCompleted: false
        },
        {
            text: "Meet friend for lunch",
            isCompleted: false
        },
        {
            text: "Build really cool todo app",
            isCompleted: false
        }
    ]);

    const addTodo = text => {
        const newTodos = [...todos, { text }];
        setTodos(newTodos)
    };

    const completeTodo = index => {
        const newTodos = [...todos];
        newTodos[index].isCompleted = true;
        setTodos(newTodos)
    }

    const removeTodo = index => {
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
                        completeTodo={() => completeTodo(index)}
                        removeTodo={() => removeTodo(index)}
                    />
                ))}
                <TodoForm addTodo={addTodo} />
            </div>
        </div>

    );
}
export default TodoLogic;