import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ text }) => (
  <div style={{
    position: 'relative', color: 'white', background: 'red',
    height: 40, width: 60, top: -20, left: -30,    
  }}>
    {text}
  </div>
);

export default class Map extends Component {
  static defaultProps = {
    center: {lat: 40.7813, lng: -73.9740},
    zoom: 11
  };

  render() {
    return (
      <GoogleMapReact
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
      >
        <AnyReactComponent
          lat={40.7813}
          lng={-73.9740}
          text={'Hack the deep!'}
        />
      </GoogleMapReact>
    );
  }
}