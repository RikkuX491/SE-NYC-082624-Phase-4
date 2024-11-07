import Hotel from './Hotel';
// import { useEffect } from 'react';
import { useOutletContext, useNavigate } from "react-router-dom";

function HotelList(){

    const {hotels, customer} = useOutletContext()

    const navigate = useNavigate()

    // useEffect(() => {
    //     if(!customer){
    //         navigate('/login')
    //     }
    // }, [customer])

    const hotelComponents = hotels.map(hotel => {
        return <Hotel key={hotel.id} hotel={hotel}/>
    })

    return (
        <ul className="hotel-list">{hotelComponents}</ul>
    );
}

export default HotelList;