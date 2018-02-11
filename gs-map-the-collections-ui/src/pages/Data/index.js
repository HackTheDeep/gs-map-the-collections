import React, { Component } from 'react';
import { Row, Col, Grid } from 'react-bootstrap';
import Dropzone from 'react-dropzone';

import './Data.css';

class Data extends Component {
  constructor(props, context) {
      super(props, context);
      this.dropFile = this.onDrop.bind(this);
  }

  onDrop(acceptedFiles, rejectedFiles) {
    console.log(acceptedFiles);

  }

  render() {
    return (
      <Grid>
        <Row>
          <Col xs={12} md={8}>
            <Dropzone onDrop={this.dropFile}>
              <div className='data-dropzone-text'>
                Drag and drop your file or click here to upload
              </div>
            </Dropzone>
          </Col>
        </Row>
      </Grid>
    );
  }
}

export default Data;
