import React, { Component } from 'react';
import { ReactiveBase, DataSearch, ResultList } from '@appbaseio/reactivesearch';

export default class SearchData extends Component {
  onData(res) {
    return {
      title: res.Coll_Subset
    }
  }

  render() {
    return (
      <ReactiveBase
        app="mapTheCollections"
        credentials="yOsE3Mn7d:caa244c4-7dfe-4441-8414-6b5cd6816e07">
        <DataSearch
            componentId="searchbox"
            dataField={['Coll_Subset', 'Family Name in Database', 'Genus Name', 'Species Name in Database', 'new_country', 'new_continent']}
            placeholder="Search me!"
            title="Search"
            highlight={true}
          />
          <ResultList
           react={{
             and: "searchbox"
           }}
           onData={this.onData}
           componentId="Results"
           dataField="Genus Name"
           />
      </ReactiveBase>
    );
  }
}
