import React from 'react';
import PropTypes from 'prop-types';

const PropertyList = ({properties}) => {
    const propertyList = properties.map((property) => 
        <p key={property.toString()}>
          {property}
        </p>
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
