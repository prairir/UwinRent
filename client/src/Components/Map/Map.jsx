import React from 'react';
import PropTypes from 'prop-types';
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";


// map styling is weird
// every `<div>` before needs height 100% for it to be variable sized
// https://stackoverflow.com/questions/16543446/how-to-make-leaflet-map-height-variable
import './Map.css';

const Map = ({properties}) => {
    const markers = properties.map((property) =>
        <Marker key={property.location.toString()}
          position={property.location.split(',').map((valStr) => Number(valStr))}>
          <Popup>
            {property.address}
            <br />
            ${property.price}
          </Popup>
        </Marker>
    );
    return (
        <MapContainer center={[42.306, -83.067]} zoom={15} scrollWheelZoom={true}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {markers}
        </MapContainer>
    );
}

Map.propTypes = {
    properties: PropTypes.array,
}

export { Map };
