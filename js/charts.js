google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart); 
    
    let b = 20

    setInterval(() => {
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Обработка поля'],
            ['Политое поле', b += .01],
            ['', 100],
        ]);
        var options = {
            backgroundColor: 'transparent',
            colors: ['#2d322d', '#4d4d4d'],
            legend: 'none',
            strokeColor: '#212121'
        };    
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));   
        chart.draw(data, options);
    }, 100)

    function drawChart() {  
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Обработка поля'],
            ['', 2],
            
            ['Политое поле', 100],
        ]);
        var options = {
          colors: ['#2d322d', '#4d4d4d'],
            backgroundColor: 'transparent',
            legend: 'none'
        };    
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));   
        chart.draw(data, options);
    }

    function randint(min, max){
      return Math.round(Math.random() * (min-max)) + min
    }


