import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import Marker from './Marker';
import { K_SIZE } from './constants';

export default class Map extends Component {
  constructor(props) {
    super(props);
    this.state = {
      markers: [
        {id: 'A', lat: 40.7813, lng: -73.9740},
        {id: 'B', lat: 40.7850, lng: -73.9740}
      ]
    }
  }

  static defaultProps = {
    center: {lat: 40.7813, lng: -73.9740},
    zoom: 16
  };

  render() {
    const places = this.state.markers
      .map(place => {
        const {id, ...coords} = place;
        return (
          <Marker key={id} {...coords} text={id}/>
        );
      });

    return (
      <GoogleMapReact
        bootstrapURLKeys={{key:'AIzaSyBfV9I1_FhnzqfmevPiNzhcJ5at2UP3Htc', language: 'en'}}
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
        hoverDistance={K_SIZE/2}
      >
        {places}
      </GoogleMapReact>
    );
  }
}