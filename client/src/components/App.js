import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const navigate = useNavigate()

    const [hotels, setHotels] = useState([])
    const [customer, setCustomer] = useState(null)

    useEffect(() => {
        // GET request - Retrieve all hotels and update the 'hotels' state with the hotel data.
        fetch('/hotels')
        .then(response => response.json())
        .then(hotelsData => setHotels(hotelsData))
    }, [])

    useEffect(() => {
        fetch('/check_session')
        .then(response => {
            if(response.ok){
                response.json().then(customerData => {
                    setCustomer(customerData)
                    if(window.location.pathname == '/login'){
                        navigate('/')
                    }
                })
            }
            else{
                navigate('/login')
            }
        })
    }, [])

    function addHotel(newHotel){
        // POST request - Create a new hotel and update the 'hotels' state to add the new hotel to the state.
        fetch('/hotels', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(newHotel)
        })
        .then(response => {
            if(response.ok){
                response.json().then(newHotelData => {
                    setHotels([...hotels, newHotelData])
                    navigate('/')
                })
            }
            else if(response.status === 400){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
            else{
                response.json().then(() => alert("Error: Something went wrong."))
            }
        })
    }

    function updateHotel(id, hotelDataForUpdate, setHotelFromHotelProfile){
        // PATCH request - Update a hotel by id and update the 'hotels' state with the updated hotel data.
        fetch(`/hotels/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(hotelDataForUpdate)
        })
        .then(response => {
            if(response.ok){
                response.json().then(updatedHotelData => {
                    setHotelFromHotelProfile(updatedHotelData)
                    setHotels(hotels => hotels.map(hotel => {
                        if(hotel.id === updatedHotelData.id){
                            return updatedHotelData
                        }
                        else{
                            return hotel
                        }
                    }))
                })
            }
            else if(response.status === 400 || response.status === 404){
                response.json().then(errorData => {
                    alert(`Error: ${errorData.error}`)
                })
            }
            else{
                response.json().then(() => {
                    alert("Error: Something went wrong.")
                })
            }
        })
    }

    function deleteHotel(id){
        // DELETE request - Delete a hotel by id and update the 'hotels' state to remove the hotel from the state.
        fetch(`/hotels/${id}`, {
            method: "DELETE"
        })
        .then(response => {
            if(response.ok){
                setHotels(hotels => hotels.filter(hotel => {
                    return hotel.id !== id
                }))
            }
            else if(response.status === 404){
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function login(loginData){
        // console.log(loginData)
        
        fetch('/login', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(loginData)
        })
        .then(response => {
            if(response.ok){
                response.json().then(customerData => {
                    setCustomer(customerData)
                    navigate('/')
                })
            }
            else{
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function logout(){
        fetch('/logout', {
            method: "DELETE"
        })
        .then(() => {
            setCustomer(null)
        })
    }

    return (
      <div className="app">
        <NavBar customer={customer} logout={logout}/>
        <Header/>
        {
            customer
            ?
            <h1>Welcome {customer.first_name} {customer.last_name}!</h1>
            :
            null
        }
        <Outlet context={
            {
                hotels: hotels,
                addHotel: addHotel,
                deleteHotel: deleteHotel,
                updateHotel: updateHotel,
                customer: customer,
                login: login
            }
        }/>
      </div>
    );
}

export default App;