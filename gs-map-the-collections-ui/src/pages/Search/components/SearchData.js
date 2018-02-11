import React, { Component } from 'react';
import { ReactiveBase, CategorySearch } from '@appbaseio/reactivesearch';

export default class SearchData extends Component {
  render() {
    return (
      <ReactiveBase
        app="mapTheCollections"
        credentials="yOsE3Mn7d:caa244c4-7dfe-4441-8414-6b5cd6816e07">
        <CategorySearch
            componentId="searchbox"
            dataField="Coll_Subset"
            categoryField="Coll_Subset.raw"
            placeholder="Search me!"
          />
      </ReactiveBase>
    );
  }
}
