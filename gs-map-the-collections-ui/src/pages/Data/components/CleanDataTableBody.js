import React, { Component } from 'react';

class CleanDataTableBody extends Component {
  constructor(props, context) {
    super(props, context);
  }

  generateRows() {
    return this.props.data.map(function(row) {

        var cells = row.map(function(cell) {

            // colData.key might be "firstName"
            return <td> {cell.toString()} </td>;
        });

        return <tr> {cells} </tr>;
    });
  }

  render() {
      const rows = this.generateRows();

    return (
        <tbody>
          {rows}
        </tbody>
    );
  }
}

export default CleanDataTableBody;
