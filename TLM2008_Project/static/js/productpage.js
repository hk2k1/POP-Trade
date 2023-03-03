function toggleHeartColor() {
    const heart = document.getElementById("heart");
    if (heart.classList.contains("red")) {
      heart.classList.remove("red");
    } else {
      heart.classList.add("red");
    }
  }

function toggleStarColor() {
    const star = document.getElementById("star");
    if (star.classList.contains("orange")) {
      star.classList.remove("orange");
    } else {
      star.classList.add("orange");
    }
  }
