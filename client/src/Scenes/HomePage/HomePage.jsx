import React from 'react';
import { Map } from '../../Components/Map';
import './HomePage.css'

const HomePage = () => {
    return (
        <div className="HomeContainer">
            <div className="Properties">
                <p>things</p>
            </div>
            <div className="Map">
                <Map/>
            </div>
        </div>
    );
}

export { HomePage };
