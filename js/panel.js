isOpened=false
function checkOpen(){
    if(isOpened==false){
        openNav()
    }
    else{
        closeNav()
    }
}

function openNav() {
document.getElementById("mySidenav").style.width = "250px";
document.getElementById("main").style.marginLeft = "250px";
document.getElementById("main_div_description").style.marginLeft = "42%";
document.getElementById("main_div_description").style.width = "58.6%"
document.getElementById("main_div_name").style.marginLeft = "42%";
document.getElementById("main_div_name").style.width = "58.6%";
document.getElementById("main_div_messages").style.marginLeft = "49.5%"
document.getElementById("main_div_errors").style.width = "29.3%";
document.getElementById("main_div_messages").style.width = "20%"
document.getElementById("mdiv").style.width = "90%";
document.getElementById("chart_div").style.marginLeft = "1340px";
document.getElementById("desc2h1").textContent = "lon: 57.34322";
document.getElementById("chart_div").style.height = "300px";
document.getElementById("chart_div").style.marginLeft = "1300px";

isOpened = true
}

function closeNav() {
document.getElementById("mySidenav").style.width = "0";
document.getElementById("main").style.marginLeft= "0";
document.getElementById("main_div_description").style.marginLeft = "37%";
document.getElementById("main_div_description").style.width = "60%";
document.getElementById("main_div_name").style.marginLeft = "37%";
document.getElementById("main_div_name").style.width = "60%";
document.getElementById("main_div_errors").style.width = "26%";
document.getElementById("main_div_messages").style.marginLeft = "37%"
document.getElementById("main_div_messages").style.width = "30%"
document.getElementById("mdiv").style.width = "90%"
document.getElementById("desc2h1").textContent = "lon: 57.84322"
document.getElementById("chart_div").style.height = "400px";
document.getElementById("chart_div").style.marginLeft = "1400px";

isOpened = false
}
