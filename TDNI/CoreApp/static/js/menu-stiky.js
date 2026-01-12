
// const navbar = document.getElementById("navbar");

// window.addEventListener("scroll", () => {
//   if (window.scrollY > 80) {
//     navbar.classList.add(
//       "bg-white",
//       "shadow-md",
//       "backdrop-blur-md"
//     );
//     navbar.classList.remove("bg-transparent");
//   } else {
//     navbar.classList.remove(
//       "bg-white",
//       "shadow-md",
//       "backdrop-blur-md"
//     );
//     navbar.classList.add("bg-transparent");
//   }
// });

// Redirection to the Hero Sections
const menuBTN = document.getElementById("menu-btn");
const heroSection = document.getElementById("hero");

menuBTN.addEventListener("click", () =>{
  menuBTN.classList.toggle('open');
  heroSection.scrollIntoView({
    behavior:'smooth',
    block:'start'
  })
})