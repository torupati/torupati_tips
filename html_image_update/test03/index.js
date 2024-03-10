function Time() {
    var realTime = new Date();
    document.getElementById("real-time-text").innerHTML = realTime.toString();
 }
 setInterval('Time()',1000);

 document.addEventListener('DOMContentLoaded', function(){
    const RELOAD_SPAN = 1000;
    function reload(){
      document.getElementById('figure').src ='figure.png' + '?' + Date.now();
    }
    setInterval(reload, RELOAD_SPAN);
  });
