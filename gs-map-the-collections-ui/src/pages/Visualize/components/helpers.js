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
    switch (specimen.classification.phylum) {
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
  let species = specimen.classification.species;

  return '<div id="content">'+
            '<h1 id="firstHeading" class="firstHeading">'+species+'</h1>'+
            '<span class="subHeading">Classification: ' + specimen.classification.phylum + '(Phylum) > '+
              specimen.classification.class + '(Class) > '+
              specimen.classification.order + '(Order) > '+
              specimen.classification.family + '(Family) > '+
              specimen.classification.phylum + '(Genus) > '+
             '</span>' + 
            '<div id="bodyContent">'+
              '<p>Collected in '+ specimen.yearCollected + ' by ' +specimen.collector.firstName + ' ' + specimen.collector.lastName +'</p>'+
            '</div>'+
          '</div>';
};

const dummyData = [{
    position: { lat: 40.7813, lng: -73.9740 }, 
    localityInfo: {
      //TBD??
    },
    classification: {
      phylum: 'Mollusca',
      class: 'Gastropoda',
      order: 'Neogastropoda ',
      family: 'Conidae',
      genus: 'Conus',
      species: 'Conus sieboldii'
    },
    collector: {
      firstName: 'John',
      lastName: 'Smith'
    }, 
    yearCollected: 1994
  },
  {
    position: { lat: 40.7813, lng: -73.9700}, 
    localityInfo: {
      //TBD??
    },
    classification: {
      phylum: 'Crustacea',
      class: 'Gastropoda',
      order: 'Neogastropoda ',
      family: 'Conidae',
      genus: 'Conus',
      species: 'Conus sieboldii 2'
    },
    collector: {
      firstName: 'John',
      lastName: 'Smith'
    }, 
    yearCollected: 1994
  },{
    position: { lat: 40.7813, lng: -73.9650}, 
    localityInfo: {
      //TBD??
    },
    classification: {
      phylum: 'Cnidaria',
      class: 'Gastropoda',
      order: 'Neogastropoda ',
      family: 'Conidae',
      genus: 'Conus',
      species: 'Conus sieboldii 2'
    },
    collector: {
      firstName: 'John',
      lastName: 'Smith'
    }, 
    yearCollected: 1994
  },
  {
    position: { lat: 40.7813, lng: -73.9710}, 
    localityInfo: {
      //TBD??
    },
    classification: {
      phylum: 'Annelida',
      class: 'Gastropoda',
      order: 'Neogastropoda ',
      family: 'Conidae',
      genus: 'Conus',
      species: 'Conus sieboldii 2'
    },
    collector: {
      firstName: 'John',
      lastName: 'Smith'
    }, 
    yearCollected: 1994
  }];

export {dummyData, determineMarkerIcon, iconClickableShape, formatInfoWindowContent};