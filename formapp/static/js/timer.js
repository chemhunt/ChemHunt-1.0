var min = 5;
var sec = 0;
function loadtimer() {
    if(localStorage.getItem("min") && localStorage.getItem("sec")) {
        min = localStorage.getItem("min");
        sec = localStorage.getItem("sec");
    }
    else {
        min = 5;
        sec = 0;
        localStorage.setItem("min", min);
        localStorage.setItem("sec",sec);
    }
    timer();
}
function timer() {

    if(sec!=0) {
        sec--;
        localStorage.setItem("sec",sec);
    }
    else {
        sec=59;
        min--;  
        localStorage.setItem("min", min);  
        localStorage.setItem("sec",sec);
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