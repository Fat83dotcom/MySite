let modal = document.getElementById("myModal");

let clickModal = document.getElementById("click-modal")

let span = document.getElementsByClassName("close")[0];

clickModal.addEventListener("click", ()=>{
    modal.style.display = "flex"
})
span.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}