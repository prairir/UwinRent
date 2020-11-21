import React from 'react';
import { MapContainer, TileLayer } from "react-leaflet";

// map styling is weird
// every `<div>` before needs height 100% for it to be variable sized
// https://stackoverflow.com/questions/16543446/how-to-make-leaflet-map-height-variable
import './Map.css'

const Map = () => {
    return (
        <MapContainer center={[42.306, -83.067]} zoom={15} scrollWheelZoom={true}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
        </MapContainer>
    );
}

export { Map };
