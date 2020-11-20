import React from 'react';
import { useQuery, gql } from '@apollo/client';

import { BrowserRouter as Router, Switch, Route, Redirect} from 'react-router-dom';

import './App.css'
import { HomePage } from '../Scenes/HomePage'

const querystuff = gql`
  query {
    hello {
      word
    }
  }
`;

const App = () => {
  const { loading, error, data } = useQuery(querystuff);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :\</p>;

  console.log(data);

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
      <p>
        {data.hello.word}
      </p>
    </div>
  );
}


export { App };
