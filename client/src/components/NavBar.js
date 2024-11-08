import { NavLink } from "react-router-dom";

function NavBar({user, logOutUser}){
    return (
        <nav className="navbar">
            {user !== null ? 
                <>
                    <NavLink to="/">Home</NavLink>
                    {user.type === 'admin' ? <NavLink to="/add_hotel">Add Hotel</NavLink> : null}
                    <NavLink to="/reviews">View All Reviews</NavLink>
                    {user.type === 'customer' ?
                    <>
                        <NavLink to="/my_reviews">My Reviews</NavLink>
                        <NavLink to="/add_review">Add Review</NavLink>
                    </>
                    :
                    null
                    }
                    <NavLink onClick={logOutUser} to="/login">Log Out</NavLink>
                </>
                :
                <>
                    <NavLink to="/login">Login</NavLink>
                    <NavLink to="/signup">Signup</NavLink>
                </>
            }
        </nav>
    )
}

export default NavBar;