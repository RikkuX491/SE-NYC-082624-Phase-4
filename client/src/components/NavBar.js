import { NavLink } from "react-router-dom";

function NavBar({customer, logout}){
    return (
        <>
            {
                customer
                ? 
                <nav className="navbar">
                    <NavLink to="/">Home</NavLink>
                    <NavLink to="/add_hotel">Add Hotel</NavLink>
                    <NavLink onClick={logout} to="/login">Log Out</NavLink>
                </nav>
                :
                null
            }
        </>
    )
}

export default NavBar;