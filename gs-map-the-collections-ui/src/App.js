import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import './App.css';

import Header from './components/Header';
import Data from './pages/Data';
import Visualize from './pages/Visualize';
import Search from './pages/Search';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header></Header>
          <Route exact path="/" component={Data} />
          <Route path="/data" component={Data} />
          <Route path="/visualize" component={Visualize} />
          <Route path="/search" component={Search} />
        </div>
      </Router>
    );
  }
}

export default App;
