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
    /* const createTask = () => {

        fetch('http://localhost:6789/tasks/', {
          method: 'POST',
          body: JSON.stringify({
            title: input
          }),
          headers: {
            "Content-type": "application/json; charset=UTF-8"
          }
        })
        setInput("")
      };
    
      const deleteTask = (id) => {
        fetch(`http://localhost:6789/tasks/${id}`, {
          method: 'DELETE',
          headers: {
            "Content-type": "application/json; charset=UTF-8"
          }
        })
        setRender(true)
      }; */
    function addTodo (text) {

        fetch('http://localhost:5000/add_data', {
            method: 'POST',
            body: JSON.stringify({
              todo: text
            }),
            headers: {
              "Content-type": "application/json; charset=UTF-8"
            }
          })
         
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