import React from 'react';
import { MapContainer, TileLayer } from "react-leaflet";
import './HomePage.css'

const HomePage = () => {
    return (
        <MapContainer center={[42.306, -83.067]} zoom={15} scrollWheelZoom={true}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
        </MapContainer>
    );
}

export { HomePage };
