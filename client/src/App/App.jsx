import React from 'react';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import './App.css'
import { HomePage } from '../Scenes/HomePage'


const App = () => {

  return (
    <div className="App">
      <Router>
        <Switch>
          <Route
            exact path="/"
            render={ () => <HomePage/> }
          />
        </Switch>
      </Router>
    </div>
  );
}


export { App };
