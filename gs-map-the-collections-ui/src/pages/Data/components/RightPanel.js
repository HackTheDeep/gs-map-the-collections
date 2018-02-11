import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import {CSVLink, CSVDownload} from 'react-csv';

import CleanDataTable from './CleanDataTable';

class RightPanel extends Component {
  constructor(props, context) {
    super(props, context);

    // TODO - convert this.props.data to csv format
    const data = this.props.data;
    const headers = Object.keys(data[0]);
    
    var csvData = [];
    csvData.push(headers);

    var rows = [];

    for(var i = 0; i < data.length; i++) {
      var keys = Object.keys(data[i]);
      var row = [];

      for(var j = 0; j < keys.length; j++) {
        row.push(data[i][keys[j]]);
      }

      rows.push(row);
      csvData.push(row);
    }

    this.state = {
      headers: headers,
      rows: rows,
      csvData: csvData
    };

    console.log(this.state.csvData);
  }

  render() {
    return (
      <div>
          <Button bsStyle="success" bsSize="small" className="data-export-button">
            <CSVLink data={this.state.csvData} >Export to CSV</CSVLink>
          </Button>
          <CleanDataTable headers={this.state.headers} rows={this.state.rows}></CleanDataTable>
      </div>
    );
  }
}

export default RightPanel;
