import { Link } from "react-router-dom";
function NavBar() {


    return (
        <div>
            <div>Home</div>
            <Link to="/Todos">Todos</Link>
        </div>
    )
}
export default NavBar;