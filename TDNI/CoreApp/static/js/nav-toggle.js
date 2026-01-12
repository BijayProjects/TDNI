const btn = document.getElementById("menu-btn");

btn.addEventListener("click", () => {
  btn.classList.toggle("active");
});

function openModal() {
  document.getElementById("modal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("modal").classList.add("hidden");
}
