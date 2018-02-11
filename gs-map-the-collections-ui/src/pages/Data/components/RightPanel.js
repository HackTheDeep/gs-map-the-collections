import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

import CleanDataTable from './CleanDataTable';

class RightPanel extends Component {

  render() {
    return (
      <div>
          <Button bsStyle="success" bsSize="small" className="data-export-button">Export to CSV</Button>
          <CleanDataTable data={this.props.data}></CleanDataTable>
      </div>
    );
  }
}

export default RightPanel;
