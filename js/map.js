//lat = 55.91366590002343
//lon = 49.284886150709525;
//alt = 96.3069;


fetch("../json/test.json")
  .then(function(resp) {
    return resp.json();
  })
  .then(function(data) {
    lat = data.current.geo0.lat;
    lon = data.current.geo0.lon;
    alt = data.current.geo0.alt;
  

    console.log(lon)
radius = (59.004496608029584 - lat) * 2;

const citymap = {
  chicago: {
    center: { lat: lat, lng: lon },
    population: radius,
  },
};

function initMap() {
  // Create the map.
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: { lat: lat, lng: lon },
    mapTypeId: "terrain",
  });

  // Construct the circle for each value in citymap.
  // Note: We scale the area of the circle based on the population.
  for (const city in citymap) {
    // Add the circle for this city to the map.
    const cityCircle = new google.maps.Circle({
      strokeColor: "rgba(0, 0, 0, 0.7)",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "rgba(0, 0, 0, 0.7)",
      fillOpacity: 0.35,
      map,
      center: citymap[city].center,
      radius: Math.sqrt(citymap[city].population) * 100,
    });
  }
}

window.initMap = initMap;
});