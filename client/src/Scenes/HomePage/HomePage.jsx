import React from 'react';
import { useQuery, gql } from '@apollo/client';

import { Map } from '../../Components/Map';
import { PropertyList } from '../../Components/PropertyList'
import './HomePage.css'

const propertiesQuery = gql`
{
  properties {
    price
    location
    address
  }
}
`;

const HomePage = () => {
  const { loading, error, data } = useQuery(propertiesQuery);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :\</p>;

  console.log(data);
  return (
    <div className="HomeContainer">
        <div className="Properties">
          <PropertyList properties={data.properties}/>
        </div>
        <div className="Map">
    <Map properties={data.properties}/>
        </div>
    </div>
  );
}

export { HomePage };
