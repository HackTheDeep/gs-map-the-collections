import React, { Component } from 'react';
import { ReactiveBase, CategorySearch } from '@appbaseio/reactivesearch';

export default class SearchData extends Component {
  render() {
    return (
      <ReactiveBase
        app="car-store"
        credentials="cf7QByt5e:d2d60548-82a9-43cc-8b40-93cbbe75c34c">
        <CategorySearch
            componentId="searchbox"
            dataField="name"
            categoryField="brand.raw"
            placeholder="Search the world!"
          />
      </ReactiveBase>
    );
  }
}
