import './App.css';
import NavBar from './NavBar';
import TodoLogic from './TodoLogic';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
function App() {

  return (

    <div className="root">
      <Router>
        <NavBar />
        <Routes>
          <Route path="/Todos" element={<TodoLogic />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
