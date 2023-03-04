let images = ["/static/img/POPtrade/WHAT_I_USED/login_slido/login_1.png",
              "/static/img/POPtrade/WHAT_I_USED/login_slido/login_2.png",
              "/static/img/POPtrade/WHAT_I_USED/login_slido/login_3.png",
              "/static/img/POPtrade/WHAT_I_USED/login_slido/login_4.png",
              "/static/img/POPtrade/WHAT_I_USED/login_slido/login_5.png",
              "/static/img/POPtrade/WHAT_I_USED/login_slido/login_6.png"];
let index = 0;
let img = document.getElementById("slideshow");

function startSlideshow() {
  setInterval(function() {
    img.classList.add("fade-out");
    setTimeout(function() {
      index = (index + 1) % images.length;
      img.src = images[index];
      img.classList.remove("fade-out");
    }, 2000);
  }, 10000);
}

startSlideshow();

var LoginForm = document.getElementById("LoginForm");
    var RegForm = document.getElementById("RegForm");
    var Indicator = document.getElementById("Indicator");

function register(){
    RegForm.style.transform = "translateX(0px)";
    LoginForm.style.transform = "translateX(0px)";
    Indicator.style.transform = "translateX(100px)";
}

function login(){
    RegForm.style.transform = "translateX(300px)";
    LoginForm.style.transform = "translateX(300px)";
    Indicator.style.transform = "translateX(0px)";
}