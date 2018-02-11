import React, { Component } from 'react';
import { Button, ButtonToolbar } from 'react-bootstrap';
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
            <div className={this.props.msg ? 'data-dropzone-text-uploaded' : 'data-dropzone-text-default'}>
            {this.props.msg ? this.props.msg : 'Drag and drop your file or click to upload'}
            </div>
        </Dropzone>
        <br></br>

        <ButtonToolbar>
          <Button
              bsStyle="primary" 
              disabled={this.props.isLoading} 
              onClick={!this.props.isLoading ? this.props.handleClick : null}
          >
              {this.props.isLoading ? 'Cleaning...' : 'Clean Data'}
          </Button>
          
          {this.props.msg ? <Button bsStyle="danger" onClick={this.props.handleClickCancel}>Cancel</Button> : ''}
        </ButtonToolbar>
      </div>
    );
  }
}

export default LeftPanel;
