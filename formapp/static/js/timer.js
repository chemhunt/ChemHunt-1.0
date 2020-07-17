var min = 60;
var sec = 0;
function loadtimer() {
    if(localStorage.getItem("min6") && localStorage.getItem("sec6")) {
        min = localStorage.getItem("min6");
        sec = localStorage.getItem("sec6");
    }
    else {
        min = 60;
        sec = 0;
        localStorage.setItem("min6", min);
        localStorage.setItem("sec6",sec);
    }
    timer();
}
function timer() {

    if(sec!=0) {
        sec--;
        localStorage.setItem("sec6",sec);
    }
    else {
        sec=59;
        min--;  
        localStorage.setItem("min6", min);  
        localStorage.setItem("sec6",sec);
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