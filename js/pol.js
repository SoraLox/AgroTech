fetch("../json/test.json")
    .then(response => response.json())
    .then(data =>{
        document.getElementById("#nameTag").innerHTML = data.clientId;
    }) 