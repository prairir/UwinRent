import React from 'react';
import ReactDOM from 'react-dom';
import { App } from './App';

import { Provider } from './Provider';

ReactDOM.render(
  <Provider>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>,
  document.getElementById('root')
);
