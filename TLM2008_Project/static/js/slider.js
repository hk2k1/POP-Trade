window.onload = function(){

    const images = ['/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/3.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/1.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/2.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/4.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/5.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/6.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/7.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/8.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/9.webp',
                    '/static/img/POPtrade/WHAT_I_USED/ZodiacSeries/10.webp'];

    let counter = 0;

    const imageElement = document.getElementById("img-js");
    const barElement = document.getElementById("slider-bar");
    barElement.style.width = "0%";
    function changeImage() {
        counter++;
        if (counter >= images.length) {
        counter = 0;
        }
        const nextImage = images[counter];
        imageElement.setAttribute("src", nextImage);
        barElement.style.width =  ((counter+1) / images.length) * imageElement.clientWidth  + "px";

    }

    let intervalId;

    imageElement.addEventListener("mouseover", function() {
      intervalId = setInterval(changeImage, 1000);
      barElement.style.display = "block";
    });

    imageElement.addEventListener("mouseout", function() {
      clearInterval(intervalId);
      imageElement.setAttribute("src", images[0]);
      barElement.style.display = "none";
      barElement.style.width = "0%";
    });


//=====================    Using Fade ==========================

//    function changeImage(){
//        counter++;
//        if(counter >= images.length){
//            counter = 0;
//        }
//        const nextImage = images[counter];
//        const tempImage = document.createElement("img");
//        tempImage.src = nextImage;
//        tempImage.style.opacity = "0";
//        tempImage.addEventListener("load", function(){
//            imageElement.style.opacity = "0";
//            imageElement.setAttribute("src", nextImage);
//            imageElement.addEventListener("transitionend", function(){
//                imageElement.style.opacity = "1";
//            });
//            barElement.style.width = ((counter+1) / images.length) * 100 + "%";
//        });
//    }
//
//    let intervalId;
//
//    imageElement.addEventListener("mouseover", function() {
//      intervalId = setInterval(changeImage, 1000);
//      barElement.style.display = "block";
//    });
//
//    imageElement.addEventListener("mouseout", function(){
//        clearInterval(intervalId);
//        imageElement.setAttribute("src", images[0]);
//        imageElement.style.opacity = "1";
//        barElement.style.display = "none";
//        barElement.style.width = "0%";
//    });

// ============= Without the slider bar - just slideshow of images ==============

//    let counter = 0;
//
//    const imageElement = document.getElementById("img-js");
//
//    function changeImage() {
//      counter++;
//      if (counter >= images.length) {
//        counter = 0;
//      }
//      const nextImage = images[counter];
//      imageElement.setAttribute("src", nextImage);
//    }
//
//    let intervalId;
//
//    imageElement.addEventListener("mouseover", function() {
//      intervalId = setInterval(changeImage, 1000);
//    });
//
//    imageElement.addEventListener("mouseout", function() {
//      clearInterval(intervalId);
//      imageElement.setAttribute("src", images[0]);
//    });


};
