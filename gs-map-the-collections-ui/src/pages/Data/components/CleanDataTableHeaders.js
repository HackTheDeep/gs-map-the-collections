import React, { Component } from 'react';

class CleanDataTableHeaders extends Component {

  generateHeaders() {
    return this.props.data.map(function(col) {
        return <th> {col} </th>;
    });
  }

  render() {
      const headers = this.generateHeaders();

    return (
        <thead>
            <tr>
            {headers}
            </tr>
        </thead>
    );
  }
}

export default CleanDataTableHeaders;
