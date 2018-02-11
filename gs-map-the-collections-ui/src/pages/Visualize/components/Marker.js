import React, { Component } from 'react';

import { K_SIZE, greatPlaceStyle, greatPlaceStyleHover,
showInfoWindowStyle, hideInfoWindowStyle } from './constants';

export default class Marker extends Component {
    constructor(props) {
        super(props);
    }

    showInfoWindow() {
        console.log("click");
    }

    render() {
        // $hover is passed in by the Google Maps API 
        const markerStyle = this.props.$hover ? greatPlaceStyleHover : greatPlaceStyle;
        const infoWindowStyle = this.props.$hover ? showInfoWindowStyle : hideInfoWindowStyle;
        
        return (
            <div className="hint hint--html hint--info hint--top" style={markerStyle}>
                <div>{this.props.text}</div>
                <div style={infoWindowStyle} className="hint__content" >
                    Сlick me
                </div>
            </div>
        );
    }
}