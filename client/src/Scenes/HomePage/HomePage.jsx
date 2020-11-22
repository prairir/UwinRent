import React from 'react';
import { useQuery, gql } from '@apollo/client';

import { Map } from '../../Components/Map';
import { PropertyList } from '../../Components/PropertyList'
import './HomePage.css'

const querystuff = gql`
  query {
    hello {
      word
    }
  }
`;

const HomePage = () => {
  const { loading, error, data } = useQuery(querystuff);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :\</p>;

  console.log(data);
  return (
    <div className="HomeContainer">
        <div className="Properties">
      <PropertyList properties={[data.hello.word, "something"]}/>
        </div>
        <div className="Map">
            <Map/>
        </div>
    </div>
  );
}

export { HomePage };
