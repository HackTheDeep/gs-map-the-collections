import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

export default class Map extends Component {
  markers = null;
  maps = null; 
  map = null; 
  bounds = null;
  markerData = null;

  static defaultProps = {
    center: { lat: 40.7813, lng: -73.9740 },
    zoom: 16
  };

  renderMarkers(map, maps) {
    // when map is first loaded
    if (this.markers === null) {
      console.log("initial load in process...");
      this.markers = [];
      this.maps = maps;
      this.map = map;
      this.bounds = this.maps.LatLngBounds();

      // make call to get dummyData 
      const dummyData = [{
        position: { lat: 40.7813, lng: -73.9740 }, 
        localityInfo: {
          //TBD??
        },
        classification: {
          phylum: 'Mollusca',
          class: 'Gastropoda',
          order: 'Neogastropoda ',
          family: 'Conidae',
          genus: 'Conus',
          species: 'Conus sieboldii'
        },
        collector: {
          firstName: 'John',
          lastName: 'Smith'
        }, 
        yearCollected: 1994
      }];

      this.markerData = dummyData;
    }

    // loop through marker data and generate a marker with a clickable info window per data point
    this.markerData.forEach((specimen) => {
      let species = specimen.classification.species;
      let contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">'+species+'</h1>'+
      '<div id="bodyContent">'+
      '<p>Collected in '+specimen.yearCollected+' by '+specimen.collector.firstName + ' ' + specimen.collector.lastName +'</p>'+
      '</div>'+
      '</div>';
      let position = new this.maps.LatLng(specimen.position.lat, specimen.position.lng);

      let marker = new this.maps.Marker({position, map: this.map, title: species});
      var infowindow = new this.maps.InfoWindow({
        content: contentString
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