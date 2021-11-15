var isImageZoomed = false;
var currentId;

function zoom(id) {
  currentId = id;
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

function zoomOutByShadow() {
  document.querySelector(".shadowbox").style.display = "none";
  document.getElementById(currentId).classList.toggle("zoomed");
  isImageZoomed = false;
}
