import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

import {dummyData, determineMarkerIcon, iconClickableShape, formatInfoWindowContent} from './helpers';
import cleanedDataJSON1 from './cleanedData';

export default class Map extends Component {
  markers = null;
  maps = null; 
  map = null; 
  bounds = null;
  markerData = null;

  static defaultProps = {
    center: { lat: 38.2693251, lng: -90.8519476 },
    zoom: 6
  };

  renderMarkers(map, maps) {
    // when map is first loaded
    if (this.markers === null) {
      console.log("initial load in process...");
      this.markers = [];
      this.maps = maps;
      this.map = map;
      this.bounds = this.maps.LatLngBounds();

      // make call to get dummyData, right now just loading a const
      this.markerData = cleanedDataJSON1;
    }

    // loop through marker data and generate a marker with a clickable info window per data point
    this.markerData.forEach((specimen) => {
      let contentString = formatInfoWindowContent(specimen);
      let position = new this.maps.LatLng(specimen.new_longitude, specimen.new_latitude);

      let marker = new this.maps.Marker({
        position, 
        map: this.map, 
        title: specimen["Species Name In Database"], 
        icon: determineMarkerIcon(specimen, this.maps), 
        shape: iconClickableShape
      });
      var infowindow = new this.maps.InfoWindow({
        content: contentString,
        maxWidth: 400
      });
      marker.addListener('click', function () {
        infowindow.open(this.map, marker);
      });
      this.markers.push(marker);
    });
  }

  render() {
    return (
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'AIzaSyBfV9I1_FhnzqfmevPiNzhcJ5at2UP3Htc', language: 'en' }}
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}
        onGoogleApiLoaded={({ map, maps }) => this.renderMarkers(map, maps)}
        yesIWantToUseGoogleMapApiInternals={true}>
      </GoogleMapReact>
    );
  }
}