import React, { Component } from 'react';

import Map from '../Visualize/components/Map';

class Visualize extends Component {
  render() {
    return (
      <div style={{ width: '100vw', height: '100vh' }}>
        <Map />
      </div>
    );
  }
}

export default Visualize;
