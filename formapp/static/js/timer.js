var min = 60;
var sec = 0;
function loadtimer() {
    if(localStorage.getItem("min3") && localStorage.getItem("sec3")) {
        min = localStorage.getItem("min3");
        sec = localStorage.getItem("sec3");
    }
    else {
        min = 60;
        sec = 0;
        localStorage.setItem("min3", min);
        localStorage.setItem("sec3",sec);
    }
    timer();
}
function timer() {

    if(sec!=0) {
        sec--;
        localStorage.setItem("sec3",sec);
    }
    else {
        sec=59;
        min--;  
        localStorage.setItem("min3", min);  
        localStorage.setItem("sec3",sec);
    }
    document.getElementById("time").innerHTML = min + ":" + (sec<10?("0"+sec):sec);
    if(sec==0 && min==0) {
        document.getElementById('time').innerHTML = "0:00";
        clearInterval(timer)     
        document.getElementById('ansbtn').click();
        alert("Time OUT!!");
    }
}
var x = setInterval(timer,1000);