import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const [hotels, setHotels] = useState([])

    useEffect(getHotels, [])

    function getHotels(){
        // GET request - Write the code to make a GET request to '/hotels' to retrieve all hotels and update the 'hotels' state with the hotel data.
        fetch("/hotels")
        .then(response => response.json())
        .then(hotelsData => setHotels(hotelsData))
    }

    function addHotel(newHotel){
        // POST request - Write the code to make a POST request to '/hotels' to create a new hotel and update the 'hotels' state to add the new hotel to the state.
        // newHotel - contains an object with the new hotel data that should be used for the POST request.
        
        // console.log(newHotel)
        fetch("/hotels", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(newHotel)
        })
        .then(response => {
            if(response.ok){
                response.json().then(newHotelData => setHotels([...hotels, newHotelData]))
            }
            else{
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function updateHotel(id, hotelDataForUpdate){
        // PATCH request - Write the code to make a PATCH request to `/hotels/${id}` (use string interpolation since the value of the id parameter should be incorporated into the string). You should update a hotel by id and update the 'hotels' state with the updated hotel data.
        // id - contains a number that refers to the id for the hotel that should be updated.
        // hotelDataForUpdate - contains an object with the hotel data for the PATCH request.

        // console.log(id)
        // console.log(hotelDataForUpdate)

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
                response.json().then(updatedHotel => {
                    const updatedHotelsArray = hotels.map(hotel => {
                        if(hotel.id === updatedHotel.id){
                            return updatedHotel
                        }
                        else{
                            return hotel
                        }
                    })

                    setHotels(updatedHotelsArray)
                })
            }
            else{
                response.json().then(errorData => alert(`Error: ${errorData.error}`))
            }
        })
    }

    function deleteHotel(id){
        // DELETE request - Write the code to make a DELETE request to `/hotels/${id}` (use string interpolation since the value of the id parameter should be incorporated into the string). You should delete a hotel by id and update the 'hotels' state to remove the hotel from the state.
        // id - contains a number that refers to the id for the hotel that should be deleted.

        // console.log(id)
        fetch(`/hotels/${id}`, {
            method: "DELETE"
        })
        .then(response => {
            if(response.ok){
                const updatedHotelsArray = hotels.filter(hotel => {
                    return hotel.id !== id
                })
                setHotels(updatedHotelsArray)
            }
            else{
                alert(`Error: Unable to delete Hotel # ${id}!`)
            }
        })
    }

    return (
      <div className="app">
        <NavBar/>
        <Header/>
        <Outlet context={{hotels: hotels, addHotel: addHotel, deleteHotel: deleteHotel, updateHotel: updateHotel}}/>
      </div>
    );
}

export default App;