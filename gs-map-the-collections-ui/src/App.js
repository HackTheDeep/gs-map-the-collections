import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import logo from './logo.svg';
import './App.css';

import Header from './components/Header';
import Data from './pages/Data';
import Visualize from './pages/Visualize';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header></Header>

          <Route exact path="/" component={Data} />
          <Route path="/data" component={Data} />
          <Route path="/visualize" component={Visualize} />

        </div>
      </Router>
    );
  }
}

export default App;
