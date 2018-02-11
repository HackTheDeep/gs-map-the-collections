import molluscaIcon from './icons/mollusca.png';
import cnidariaIcon from './icons/cnidaria.png';
import crustaceaIcon from './icons/crustacea.png';
import annelidaIcon from './icons/annelida.png';

// Shapes define the clickable region of the icon. The type defines an HTML
// <area> element 'poly' which traces out a polygon as a series of X,Y points.
// The final coordinate closes the poly by connecting to the first coordinate.
const iconClickableShape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: 'poly'
};

var determineMarkerIcon = function(specimen, mapsInstance) {
    var imageUrl = '';
    switch (specimen['Coll_Subset']) {
        case 'Mollusca':
          imageUrl = molluscaIcon;
          break;
        case 'Cnidaria':
          imageUrl = cnidariaIcon;
          break;
        case 'Crustacea':
          imageUrl = crustaceaIcon;
          break;
        case 'Annelida':
          imageUrl = annelidaIcon;
          break;
        case 'Other Invertebrate Phyla':
    }

    // create custom shell marker 
    // Origins, anchor positions and coordinates of the marker increase in the X
    // direction to the right and in the Y direction down.
    var image = {
        url: imageUrl,
        size: new mapsInstance.Size(32, 32),
        // The origin for this image is (0, 0).
        origin: new mapsInstance.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new mapsInstance.Point(0, 0)
      };
  
    return image;
};

var formatInfoWindowContent = function(specimen) {
  let species = specimen['Species Name in Database'];
  let year = specimen['Species Year'];
  if (year.length > 4) {
    year.slice(0,-1);
  }
  const recordInfo = JSON.stringify(specimen, undefined, 2);

  return '<div id="content">'+
            '<h1 id="firstHeading" class="firstHeading">'+species+'</h1>'+
            '<div id="bodyContent" class="infoWindow--Body">'+
              '<p>Record information:</p>'+ 
                '<pre>'+recordInfo+'</pre>'+
            '</div>'+
          '</div>';
};


// const dummyData = [{
//     position: { lat: 40.7813, lng: -73.9740 }, 
//     localityInfo: {
//       //TBD??
//     },
//     classification: {
//       phylum: 'Mollusca',
//       class: 'Gastropoda',
//       order: 'Neogastropoda ',
//       family: 'Conidae',
//       genus: 'Conus',
//       species: 'Conus sieboldii'
//     },
//     collector: {
//       firstName: 'John',
//       lastName: 'Smith'
//     }, 
//     yearCollected: 1994
//   },
//   {
//     position: { lat: 40.7813, lng: -73.9700}, 
//     localityInfo: {
//       //TBD??
//     },
//     classification: {
//       phylum: 'Crustacea',
//       class: 'Gastropoda',
//       order: 'Neogastropoda ',
//       family: 'Conidae',
//       genus: 'Conus',
//       species: 'Conus sieboldii 2'
//     },
//     collector: {
//       firstName: 'John',
//       lastName: 'Smith'
//     }, 
//     yearCollected: 1994
//   },{
//     position: { lat: 40.7813, lng: -73.9650}, 
//     localityInfo: {
//       //TBD??
//     },
//     classification: {
//       phylum: 'Cnidaria',
//       class: 'Gastropoda',
//       order: 'Neogastropoda ',
//       family: 'Conidae',
//       genus: 'Conus',
//       species: 'Conus sieboldii 2'
//     },
//     collector: {
//       firstName: 'John',
//       lastName: 'Smith'
//     }, 
//     yearCollected: 1994
//   },
//   {
//     position: { lat: 40.7813, lng: -73.9710}, 
//     localityInfo: {
//       //TBD??
//     },
//     classification: {
//       phylum: 'Annelida',
//       class: 'Gastropoda',
//       order: 'Neogastropoda ',
//       family: 'Conidae',
//       genus: 'Conus',
//       species: 'Conus sieboldii 2'
//     },
//     collector: {
//       firstName: 'John',
//       lastName: 'Smith'
//     }, 
//     yearCollected: 1994
//   }];

const dummyData = [{
  "Tracking Number": "M70608",
  "Coll_Subset": "Mollusca",
  "Family Name in Database": "Unionidae",
  "Genus Name": "Epioblasma",
  "Species Name in Database": "triquetra",
  "Species Year": "1820)",
  "new_continent": "",
  "new_country": "United States",
  "new_department / Province / State": "Missouri",
  "new_county": "Valley Park",
  "new_coordinates": "('38.2693251', '-90.8519476')",
  "new_longitude": 38.2693251,
  "new_latitude": -90.8519476
}];

export {dummyData, determineMarkerIcon, iconClickableShape, formatInfoWindowContent};