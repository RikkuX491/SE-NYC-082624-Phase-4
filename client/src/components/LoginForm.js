import { useState } from "react";

import { useOutletContext } from "react-router-dom";

function LoginForm(){

    const [username, setUsername] = useState("")

    const {login} = useOutletContext()

    function updateUsername(event){
        setUsername(event.target.value)
    }

    function handleSubmit(event){
        event.preventDefault()
        login({username: username})
    }

    return (
        <div className="new-hotel-form">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input onChange={updateUsername} type="text" name="username" placeholder="Username" value={username} required />
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default LoginForm;