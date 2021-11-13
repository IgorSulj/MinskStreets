var isImageZoomed = false;

function zoom(id) {
  if (!isImageZoomed) {
    document.getElementById(id).classList.toggle("zoomed");
    document.querySelector(".shadowbox").style.display = "block";
    isImageZoomed = true;
  } else {
    document.getElementById(id).classList.toggle("zoomed");
    document.querySelector(".shadowbox").style.display = "none";
    isImageZoomed = false;
  }
}