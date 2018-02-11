import React, { Component } from 'react';

import Map from '../Visualize/components/Map';

class Visualize extends Component {
  render() {
    return (
      <div style={{ width: '99vw', height: '99vh' }}>
        <Map />
      </div>
    );
  }
}

export default Visualize;
