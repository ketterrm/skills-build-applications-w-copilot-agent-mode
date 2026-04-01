import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';

// Get codespace name from environment variable
const codespaceName = process.env.REACT_APP_CODESPACE_NAME;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App codespaceName={codespaceName} />
    </BrowserRouter>
  </React.StrictMode>
);

reportWebVitals();
