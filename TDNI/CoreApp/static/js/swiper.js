
new Swiper(".serviceSwiper", {
  slidesPerView: 1,
  spaceBetween: 24,
  loop: true,
  speed: 800,


  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  effect: "slide",
  grabCursor: true,
  resistanceRatio: 0.6,
  threshold: 10,

  // smooth easing
  cssMode: false,

  breakpoints: {
    640: {
      slidesPerView: 1.2,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

// Our wokr Swiper

const swiper = new Swiper(".mySwiper", {
      slidesPerView: 3,
      spaceBetween: 30,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

