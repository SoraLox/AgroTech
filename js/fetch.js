fetch("../json/test.json")
  .then(function(resp) {
    return resp.json();
  })
  .then(function(data) {

    
    console.log(data.current.mag1.angle);
    console.log(Math.sqrt((((data.current.geo0.lat - data.start.geo0.lat)*(data.current.geo0.lat - data.start.geo0.lat) + (data.current.geo0.lon - data.start.geo0.lon)*(data.current.geo0.lon - data.start.geo0.lon)) * 111 * 1000)));

    strelka.style.transform = 'rotate(' + data.current.mag1.angle + 'deg)';

    dg.textContent = data.current.mag1.angle;

    ms.textContent = Math.sqrt((((data.current.geo0.lat - data.start.geo0.lat)*(data.current.geo0.lat - data.start.geo0.lat) + (data.current.geo0.lon - data.start.geo0.lon)*(data.current.geo0.lon - data.start.geo0.lon)) * 111 * 1000)) + "m\\s";

    desc2h1.textContent = "lon: " + data.current.geo0.lon;
    desc2h11.textContent = "len: " + data.current.geo0.lat;

    pressure.textContent = data.waterPressure + " ";

    time.textContent = data.workTime  / 3600 + " hours";

    nameTag.textContent = data.clientId + " " + data.contractVer

  });
