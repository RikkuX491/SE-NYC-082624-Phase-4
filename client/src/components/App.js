import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import NavBar from "./NavBar";

function App(){

    const [hotels, setHotels] = useState([])

    useEffect(getHotels, [])

    function getHotels(){
        // Deliverable # 2 solution code
        fetch("/hotels")
        .then(response => response.json())
        .then(hotelsData => setHotels(hotelsData))
    }

    function addHotel(newHotel){
        // Deliverable # 3 solution code
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
        })
    }

    function updateHotel(id, hotelDataForUpdate){
        // Deliverable # 4 solution code
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
        })
    }

    function deleteHotel(id){
        // Deliverable # 5 solution code
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