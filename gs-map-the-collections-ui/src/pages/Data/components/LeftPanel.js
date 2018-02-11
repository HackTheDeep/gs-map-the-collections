import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import Dropzone from 'react-dropzone';

class LeftPanel extends Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      showError: false
    };
  }

  render() {
    return (
      <div>
        <Dropzone onDrop={this.props.onDrop}>
            <div className='data-dropzone-text'>
            {this.props.msg ? this.props.msg : 'Drag and drop your file or click to upload'}
            </div>
        </Dropzone>
        <br></br>
        <Button
            bsStyle="primary" 
            disabled={this.props.isLoading} 
            onClick={!this.props.isLoading ? this.props.handleClick : null}
        >
            {this.props.isLoading ? 'Cleaning...' : 'Clean Data'}
        </Button>
      </div>
    );
  }
}

export default LeftPanel;
