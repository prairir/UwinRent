import React from 'react';
import PropTypes from 'prop-types';

import HouseIcon from './house.svg'
import './PropertyList.css'

const PropertyList = ({properties}) => {
    const propertyList = properties.map((property) => 
        <div className="House" key={property.location.address.toString()}>
            <img src={HouseIcon} alt="House Icon" className="HouseIcon" /> <br/>
            {property.location.address}
            <br/>
            ${property.price}
        </div>
    );

    return (
        <div className="Properties">
            <h1>
                Properties
            </h1>
            <div className="PropertyList">
              {propertyList}
            </div>
        </div>
    );
}

PropertyList.propTypes = {
    properties: PropTypes.array.isRequired,
}

export { PropertyList };
