import React, { Component } from 'react';
import { Table } from 'react-bootstrap';

import CleanDataTableHeaders from './CleanDataTableHeaders';
import CleanDataTableBody from './CleanDataTableBody';

class CleanDataTable extends Component {
  // constructor(props, context) {
  //   super(props, context);

  //   const data = this.props.data;
  //   const headers = Object.keys(data[0]);

  //   var rows = [];

  //   for(var i = 0; i < data.length; i++) {
  //     var keys = Object.keys(data[i]);
  //     var row = [];

  //     for(var j = 0; j < keys.length; j++) {
  //       row.push(data[i][keys[j]]);
  //     }

  //     rows.push(row);
  //   }

  //   this.state = {
  //     headers: headers,
  //     rows: rows
  //   };
  // }

  render() {
    return (
      <Table responsive>
        <CleanDataTableHeaders data={this.props.headers}></CleanDataTableHeaders>
        <CleanDataTableBody data={this.props.rows}></CleanDataTableBody>
      </Table>
    );
  }
}

export default CleanDataTable;
