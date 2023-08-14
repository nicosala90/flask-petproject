function Todo (props){
    return(
        <div
        className="todo"
        style={{ textDecoration: props.todo.isCompleted ? "line-through" : "" }}
      >
        {props.todo.text}
        <div>
          <button onClick={() => props.completeTodo()}>Complete</button>
          <button onClick={() => props.removeTodo()}>X</button>
        </div>
      </div>
    );
}

export default Todo;